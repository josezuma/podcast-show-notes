#!/usr/bin/env python3
"""podcast-show-notes — Show notes generator from audio transcripts. Timestamps, key points, links."""
import sys, json, argparse

def main():
    parser = argparse.ArgumentParser(description="Show notes generator from audio transcripts. Timestamps, key points, links.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    
    result = {"tool": "podcast-show-notes", "status": "ready", "version": "1.0.0", "author": "Jose Zuma"}
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"{result['tool']} v{result['version']} — {result['status']}")

if __name__ == "__main__":
    main()
