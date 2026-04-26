#!/usr/bin/env python3
"""Collect a quick workstation/server health summary."""

from __future__ import annotations

import datetime as dt
import platform
import socket

import psutil


def bytes_to_gib(value: int) -> float:
    return round(value / (1024**3), 2)


def main() -> None:
    boot_time = dt.datetime.fromtimestamp(psutil.boot_time())
    uptime = dt.datetime.now() - boot_time
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print("IT Support Health Check")
    print("=" * 24)
    print(f"Host: {socket.gethostname()}")
    print(f"OS: {platform.platform()}")
    print(f"Boot time: {boot_time:%Y-%m-%d %H:%M:%S}")
    print(f"Uptime: {str(uptime).split('.')[0]}")
    print()
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory usage: {memory.percent}% ({bytes_to_gib(memory.used)} / {bytes_to_gib(memory.total)} GiB)")
    print(f"Disk usage: {disk.percent}% ({bytes_to_gib(disk.used)} / {bytes_to_gib(disk.total)} GiB)")

    if memory.percent >= 90:
        print("WARNING: Memory usage is high.")
    if disk.percent >= 90:
        print("WARNING: Disk usage is high.")


if __name__ == "__main__":
    main()
