import requests
import re
import urllib.parse

def test_gwt_request():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    })

    print("Fetching Shop.html...")
    resp = session.get("https://peak.smarthub.coop/Shop.html")
    print("Cookies:", session.cookies.get_dict())
    
    # Shop.html should load the smarthub GWT module
    # Look for nocache.js inclusion, usually like <script src="smarthub/smarthub.nocache.js"></script>
    match = re.search(r'src=["\']([^"\']+\.nocache\.js.*?)["\']', resp.text)
    if not match:
        print("Could not find nocache.js in Shop.html")
        return
        
    nocache_url = urllib.parse.urljoin("https://peak.smarthub.coop/Shop.html", match.group(1))
    print("Found nocache JS:", nocache_url)
    
    resp_nocache = session.get(nocache_url)
    nocache_js = resp_nocache.text
    
    with open("nocache_dump.js", "w", encoding="utf-8") as f:
        f.write(nocache_js)
    
    # Check for permutation arrays in the dump
    permutations = re.findall(r"['\"]([A-F0-9]{32})['\"]", nocache_js)
    if not permutations:
        print("Could not find any 32-char hex permutation IDs in nocache.js")
        return
        
    print(f"Found permutation IDs: {permutations}")
    
    target_cache_url = None
    target_permutation = None
    for pm in permutations:
        cache_url = urllib.parse.urljoin("https://peak.smarthub.coop/", f"{pm}.cache.js")
        print(f"Fetching cache JS: {cache_url}")
        resp_cache = session.get(cache_url)
        
        with open(f"cache_{pm}.js", "w", encoding="utf-8") as f:
            f.write(resp_cache.text)
            
        # In GWT, RPC methods are registered with their hash.
        # We can look for the getAddressForMember hash we saw: B5942E1CFECF3F9B862E631514ED7F93
        if "B5942E1CFECF3F9B862E631514ED7F93" in resp_cache.text:
            print("FOUND KNOWN HASH B5942E1CFECF3F9B862E631514ED7F93 IN:", pm)
        
        if "getAddressForMember" in resp_cache.text:
            print("FOUND getAddressForMember in:", pm)
            with open("cache_dump.js", "w", encoding="utf-8") as f:
                f.write(resp_cache.text)
            
        # Let's try the regex to dynamically find the hash
        rpc_match = re.search(r"['\"]([A-F0-9]{32})['\"],\s*['\"]coop\.nisc\.consumer\.common\.client\.service\.MemberService['\"],\s*['\"]getAddressForMember['\"]", resp_cache.text)
        if rpc_match:
            rpc_hash = rpc_match.group(1)
            print(f"SUCCESS! Dynamically extracted getAddressForMember RPC Hash: {rpc_hash} from permutation {pm}")
            target_cache_url = cache_url
            target_permutation = pm
            break
            
    if not target_permutation:
        print("Could not find the RPC hash for getAddressForMember in any cache file.")
        return
        
    print("\n--- Trying to make the RPC call ---")
    rpc_url = "https://peak.smarthub.coop/gwt/MemberService"
    
    # We also need a strong name for the request header x-gwt-permutation
    headers = {
        'Accept': '*/*',
        'Content-Type': 'text/x-gwt-rpc; charset=UTF-8',
        'X-GWT-Module-Base': 'https://peak.smarthub.coop/',
        'X-GWT-Permutation': target_permutation,
        'Origin': 'https://peak.smarthub.coop',
        'Referer': 'https://peak.smarthub.coop/Shop.html',
    }
    
    # Let's see if we can just mimic the payload from the network trace, but swap the hash
    # The original was: 7|0|4|https://peak.smarthub.coop/|B5942E1CFECF3F9B862E631514ED7F93|coop.nisc.consumer.common.client.service.MemberService|getAddressForMember|1|2|3|4|0|
    payload = f"7|0|4|https://peak.smarthub.coop/|{rpc_hash}|coop.nisc.consumer.common.client.service.MemberService|getAddressForMember|1|2|3|4|0|"
    
    print("Request Headers:", headers)
    print("Payload:", payload)
    
    resp_rpc = session.post(rpc_url, headers=headers, data=payload)
    print("Response Status:", resp_rpc.status_code)
    print("Response Body:", resp_rpc.text)
    
if __name__ == "__main__":
    test_gwt_request()
