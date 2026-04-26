#!/usr/bin/env python3
"""Run simple DNS and connectivity checks for support triage."""

from __future__ import annotations

import argparse
import platform
import socket
import subprocess
from dataclasses import dataclass


@dataclass
class HostResult:
    host: str
    resolved_ip: str | None
    ping_ok: bool


def resolve_host(host: str) -> str | None:
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None


def ping_host(host: str) -> bool:
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", count_flag, "2", host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return result.returncode == 0


def check_host(host: str) -> HostResult:
    resolved_ip = resolve_host(host)
    return HostResult(host=host, resolved_ip=resolved_ip, ping_ok=ping_host(host))


def main() -> None:
    parser = argparse.ArgumentParser(description="Check DNS resolution and ping reachability.")
    parser.add_argument(
        "--hosts",
        nargs="+",
        default=["google.com", "cloudflare.com", "github.com"],
        help="Hostnames or IP addresses to check.",
    )
    args = parser.parse_args()

    print("Network Check")
    print("=" * 13)
    for result in [check_host(host) for host in args.hosts]:
        dns_status = result.resolved_ip or "DNS FAILED"
        ping_status = "OK" if result.ping_ok else "FAILED"
        print(f"{result.host:<30} DNS: {dns_status:<16} Ping: {ping_status}")


if __name__ == "__main__":
    main()
