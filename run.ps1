param(
    [string]$file
)

if (-not $file) {
    Write-Output "Error: file name required"
    exit 1
}

$match = Get-ChildItem -Path . -Recurse -File -Filter $file -ErrorAction SilentlyContinue | Select-Object -First 1
$file_path = if ($match) { Resolve-Path -Relative $match.FullName } else { "" }

Write-Output "Executing $file_path"

uv run $file_path test run
