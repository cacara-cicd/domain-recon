#!/usr/bin/env python3
"""Resolve domains in domains.txt to IPv4 addresses and write ips.txt."""
import socket
import sys

INPUT = "domains.txt"
OUTPUT = "ips.txt"

def main() -> int:
    try:
        with open(INPUT, "r") as f:
            domains = [
                line.strip()
                for line in f
                if line.strip() and not line.startswith("#")
            ]
    except FileNotFoundError:
        print(f"ERROR: {INPUT} not found")
        return 1

    resolved, failed = [], []
    for domain in domains:
        try:
            ip = socket.gethostbyname(domain)
            resolved.append(ip)
            print(f"[OK]   {domain} -> {ip}")
        except socket.gaierror:
            failed.append(domain)
            print(f"[FAIL] {domain}")

    with open(OUTPUT, "w") as f:
        for ip in resolved:
            f.write(ip + "\n")

    print(f"\nResolved: {len(resolved)}  Failed: {len(failed)}")
    if failed:
        print("Unresolved domains:")
        for d in failed:
            print(f"  - {d}")

    return 0 if resolved else 1

if __name__ == "__main__":
    sys.exit(main())