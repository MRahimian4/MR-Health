# -*- coding: utf-8 -*-
"""
MR.Health - Live Web Application Runner & Public Tunnel Launcher
Starts FastAPI on port 8000 and establishes a live public HTTPS URL via LocalTunnel.
"""
import os
import sys
import time
import re
import subprocess
import webbrowser
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

def main():
    print("=" * 65)
    print("  🚀 MR.Health AI — Live Web Application Launcher")
    print("  Multimodal Medical Analytics powered by Google Gemini 3.8 Flash")
    print("=" * 65)

    port = 8000
    host = "127.0.0.1"

    # 1. Start FastAPI / Uvicorn Server in background
    print(f"\n[1/3] Starting FastAPI local server on http://{host}:{port}...")
    server_cmd = [sys.executable, "-m", "uvicorn", "app:app", "--host", host, "--port", str(port)]
    server_proc = subprocess.Popen(
        server_cmd,
        cwd=str(PROJECT_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    # Give server 2 seconds to bind
    time.sleep(2)
    local_url = f"http://{host}:{port}"
    print(f"      Local Server is online at: {local_url}")

    # 2. Launch LocalTunnel for Live Public URL
    print("\n[2/3] Establishing live public HTTPS tunnel (localtunnel)...")
    tunnel_cmd = ["npx.cmd", "--yes", "localtunnel", "--port", str(port)]
    try:
        tunnel_proc = subprocess.Popen(
            tunnel_cmd,
            cwd=str(PROJECT_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
    except Exception as e:
        print(f"      Warning: Could not launch npx localtunnel: {e}")
        tunnel_proc = None

    public_url = None
    if tunnel_proc:
        # Read lines to find public URL
        start_time = time.time()
        while time.time() - start_time < 15:
            line = tunnel_proc.stdout.readline()
            if not line:
                time.sleep(0.5)
                continue
            if "your url is:" in line.lower():
                m = re.search(r"https://[^\s]+", line)
                if m:
                    public_url = m.group(0).strip()
                    break

    # 3. Present URLs
    print("\n[3/3] Application is LIVE!")
    print("=" * 65)
    if public_url:
        print(f"  🌐 LIVE PUBLIC URL:  {public_url}")
    else:
        print(f"  🌐 LIVE PUBLIC URL:  (Generating... check localtunnel)")
    print(f"  🏠 LOCAL WEB URL:    {local_url}")
    print("=" * 65)
    print("\nReady to accept checkup scans, 1-minute voice notes, and clinical instructions.")
    print("Press Ctrl+C to terminate the live server.\n")

    # Open live URL or local URL
    target_url = public_url if public_url else local_url
    webbrowser.open(target_url)

    try:
        # Keep running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server and tunnel...")
        server_proc.terminate()
        if tunnel_proc:
            tunnel_proc.terminate()
        print("Shutdown complete.")

if __name__ == "__main__":
    main()
