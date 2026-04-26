#!/usr/bin/env bash
set -euo pipefail

echo "Linux Audit"
echo "==========="
echo "Hostname: $(hostname)"
echo "Kernel: $(uname -r)"
echo "OS:"
if [[ -f /etc/os-release ]]; then
  . /etc/os-release
  echo "  ${PRETTY_NAME:-Unknown}"
else
  echo "  Unknown"
fi

echo
echo "Uptime:"
uptime

echo
echo "Disk usage:"
df -h /

echo
echo "Memory:"
free -h

echo
echo "Top CPU processes:"
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 10

echo
echo "Listening ports:"
if command -v ss >/dev/null 2>&1; then
  ss -tulpen
else
  netstat -tulpen
fi
