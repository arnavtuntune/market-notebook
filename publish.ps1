# Publish this month's work to GitHub.
# Run after you've written "What I learned" in the report and/or added a note:
#     .\publish.ps1 "October report + HDFC Bank note"

param([string]$Message = "Monthly update $(Get-Date -Format 'MMMM yyyy')")

Set-Location $PSScriptRoot

$report = Join-Path "reports" "$(Get-Date -Format 'yyyy-MM').md"
if ((Test-Path $report) -and (Select-String -Path $report -Pattern "_Write 3–5 sentences yourself" -Quiet)) {
    Write-Host "Write your 'What I learned' section in $report first." -ForegroundColor Yellow
    exit 1
}

git add -A
git commit -m $Message
git push
