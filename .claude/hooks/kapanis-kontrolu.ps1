$girdi = [Console]::In.ReadToEnd() | ConvertFrom-Json
if ($girdi.stop_hook_active) { exit 0 }

$degisen = @(git status --porcelain 2>$null)
if ($degisen.Count -eq 0) { exit 0 }

$kod = $degisen | Where-Object { $_ -notmatch 'CHANGELOG\.md|TODO\.md' }
if (-not $kod) { exit 0 }

$log = $degisen | Where-Object { $_ -match 'CHANGELOG\.md' }
if ($log) { exit 0 }

$mesaj = "Degisiklik var ama CHANGELOG.md guncellenmemis. PROJECT.md bolum 8 - CHANGELOG ve paket durumu guncellenmeden is tamamlanmis sayilmaz."
$temp = Get-ChildItem -Path 'temp' -Directory -ErrorAction SilentlyContinue
if ($temp) { $mesaj += " Ayrica temp/ dolu: " + ($temp.Name -join ', ') }

[Console]::Error.WriteLine($mesaj)
exit 2
