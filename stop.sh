#!/bin/bash

echo "Stopping PEAK Internet local server..."

if [ -f .server_pid ]; then
    PID=$(cat .server_pid)
    
    # Check if process is still running
    if ps -p $PID > /dev/null; then
        kill $PID
        echo "Server (PID $PID) stopped."
    else
        echo "Server is not running (PID $PID not found)."
    fi
    
    rm .server_pid
else
    # Fallback to finding the python http.server process
    OPID=$(lsof -t -i :8000)
    if [ ! -z "$OPID" ]; then
        kill $OPID
        echo "Server (PID $OPID) stopped."
    else
        echo "No server found running on port 8000."
    fi
fi
