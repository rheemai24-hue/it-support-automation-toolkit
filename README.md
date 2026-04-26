# IT Support Automation Toolkit

A small cross-platform toolkit for common IT support checks and cleanup tasks.

## Project Layout

```text
scripts/
  health_check.py      System health summary for CPU, memory, disk, and uptime
  network_check.py     Connectivity and DNS checks
  cleanup_temp.ps1     Windows temp-file cleanup helper
  linux_audit.sh       Linux host audit summary
reports/               Generated reports and command output
requirements.txt       Python dependencies
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run a system health check:

```bash
python scripts/health_check.py
```

Run network checks:

```bash
python scripts/network_check.py --hosts google.com cloudflare.com github.com
```

Run a Linux audit:

```bash
bash scripts/linux_audit.sh
```

Run Windows temporary file cleanup in PowerShell:

```powershell
.\scripts\cleanup_temp.ps1 -WhatIf
.\scripts\cleanup_temp.ps1
```

## Reports

Generated outputs can be stored in the `reports/` directory. The directory is kept in git with a `.gitkeep` file.
