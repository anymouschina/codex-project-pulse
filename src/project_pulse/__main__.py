"""Run with python3 -m project_pulse from the src directory."""
import json

from .launch import launch


if __name__ == "__main__":
    print(json.dumps(launch(), ensure_ascii=False))
