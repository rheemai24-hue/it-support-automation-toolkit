param(
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"

$targets = @(
    $env:TEMP,
    "C:\Windows\Temp"
) | Where-Object { $_ -and (Test-Path $_) } | Select-Object -Unique

Write-Host "Windows Temporary File Cleanup"
Write-Host "=============================="

foreach ($target in $targets) {
    Write-Host "Scanning $target"
    $items = Get-ChildItem -Path $target -Force -ErrorAction SilentlyContinue

    foreach ($item in $items) {
        try {
            if ($WhatIf) {
                Write-Host "Would remove: $($item.FullName)"
            }
            else {
                Remove-Item -Path $item.FullName -Recurse -Force -ErrorAction Stop
                Write-Host "Removed: $($item.FullName)"
            }
        }
        catch {
            Write-Warning "Skipped $($item.FullName): $($_.Exception.Message)"
        }
    }
}

Write-Host "Cleanup complete."
