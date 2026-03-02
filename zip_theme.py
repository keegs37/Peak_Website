import zipfile
import os

def zip_theme(folder_path, output_path):
    print(f"Zipping {folder_path} to {output_path}...")
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Ensure the root of the zip contains the folder `peak-theme`
                arcname = os.path.relpath(file_path, os.path.dirname(folder_path))
                zipf.write(file_path, arcname)
                
    print("Zipping complete.")

if __name__ == '__main__':
    zip_theme('peak-theme', 'peak-theme.zip')
