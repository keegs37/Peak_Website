#!/bin/bash

echo "Starting PEAK Internet local server..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH."
    echo "Please install Python 3 to run the local server."
    exit 1
fi

# Check if server is already running
if lsof -i :8000 > /dev/null; then
    echo "A server is already running on port 8000."
    exit 1
fi

# Start the server in the background and save the PID
nohup python3 -m http.server 8000 > server.log 2>&1 &
PID=$!
echo $PID > .server_pid

echo "Server started at http://localhost:8000"
echo "Log output is being saved to server.log"
echo "Use ./stop.sh to stop the server."
