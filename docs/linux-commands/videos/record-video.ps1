# ============================================================
# RECORD-VIDEO.PS1 - Quay video demo Linux Commands
# Cách dùng: .\record-video.ps1
# Yêu cầu: asciinema đã cài trong WSL Ubuntu
# ============================================================

Write-Host "🎬 Bắt đầu quay video Linux Commands Demo..." -ForegroundColor Cyan

$projectPath = "E:\DevOps\my-project"
$videoDir = "$projectPath\docs\linux-commands\videos"
$castFile = "$videoDir\linux-commands-demo.cast"
$scriptPath = "$videoDir\demo-script.sh"

# Convert path to WSL format
$wslVideoDir = "/mnt/e/DevOps/my-project/docs/linux-commands/videos"
$wslScriptPath = "/mnt/e/DevOps/my-project/docs/linux-commands/videos/demo-script.sh"
$wslCastPath = "$wslVideoDir/linux-commands-demo-recorded.cast"

Write-Host ""
Write-Host "📁 Video sẽ được lưu tại:" -ForegroundColor Yellow
Write-Host "   $castFile" -ForegroundColor White
Write-Host ""

# Kiểm tra asciinema
$hasAsciinema = wsl -d Ubuntu -- bash -c "which asciinema 2>/dev/null"
if ($hasAsciinema) {
    Write-Host "✅ asciinema đã được cài đặt: $hasAsciinema" -ForegroundColor Green
    Write-Host ""
    Write-Host "🔴 Đang record..." -ForegroundColor Red

    # Record
    wsl -d Ubuntu -- bash -c "cd ~ && asciinema rec $wslCastPath --command 'bash $wslScriptPath' --title 'Linux Commands cho DevOps' --idle-time-limit 2"

    Write-Host ""
    Write-Host "✅ Quay video hoàn tất!" -ForegroundColor Green
    Write-Host "📁 File: $wslCastPath" -ForegroundColor Cyan
} else {
    Write-Host "⚠️  asciinema chưa được cài. Đang cài đặt..." -ForegroundColor Yellow
    wsl -d Ubuntu -- bash -c "sudo apt-get install -y asciinema"
    Write-Host "✅ Cài xong! Chạy lại script này để record." -ForegroundColor Green
}

Write-Host ""
Write-Host "💡 Để xem video:" -ForegroundColor Cyan
Write-Host "   wsl -d Ubuntu -- asciinema play $wslCastPath" -ForegroundColor White
Write-Host ""
Write-Host "💡 Để upload lên asciinema.org:" -ForegroundColor Cyan
Write-Host "   wsl -d Ubuntu -- asciinema upload $wslCastPath" -ForegroundColor White
