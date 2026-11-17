#!/usr/bin/env python3
"""Start or reuse the loopback dashboard, returning a verified local URL."""
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent


def launch(port=4318):
    url = f"http://127.0.0.1:{port}"

    def check():
        try:
            with urlopen(url + "/api/health", timeout=1) as response:
                return json.load(response).get("service") == "codex-project-pulse"
        except (URLError, TimeoutError, ValueError):
            return False

    if check():
        return {"url": url, "running": True}
    directory = Path(os.environ.get("PULSE_DATA_DIR") or Path.home() / ".local/share/codex-project-pulse")
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    with (directory / "server.log").open("ab") as logfile:
        process = subprocess.Popen([sys.executable, "-m", "project_pulse.server", "--port", str(port)], cwd=ROOT.parent, stdin=subprocess.DEVNULL, stdout=logfile, stderr=logfile, start_new_session=True)
    for _ in range(30):
        if check():
            return {"url": url, "running": True}
        if process.poll() is not None:
            raise RuntimeError("总控台启动失败：端口可能被占用，请检查插件 server.log")
        time.sleep(0.1)
    raise RuntimeError("总控台未在预期时间内就绪，请查看插件 server.log")


if __name__ == "__main__":
    print(json.dumps(launch(), ensure_ascii=False))
