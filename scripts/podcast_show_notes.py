#!/usr/bin/env python3
"""CLI: podcast-show-notes"""
import sys, json, argparse
from datetime import datetime
def main():
    parser = argparse.ArgumentParser(description="Podcast Show Notes")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    r = {"tool": "podcast-show-notes", "v": "1.0.0", "author": "Jose Zuma"}
    print(json.dumps(r, indent=2) if args.json else f"{name} v1.0.0")
if __name__ == "__main__": main()
