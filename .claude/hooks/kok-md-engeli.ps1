$girdi = [Console]::In.ReadToEnd() | ConvertFrom-Json
$yol = $girdi.tool_input.file_path
if (-not $yol) { exit 0 }
if ($yol -notmatch '\.md$') { exit 0 }

$tam = [System.IO.Path]::GetFullPath($yol)
$dizin = [System.IO.Path]::GetDirectoryName($tam)
if ($dizin -ne (Get-Location).Path) { exit 0 }

$beyazListe = @('PROJECT.md','CLAUDE.md','AGENTS.md','TODO.md','CHANGELOG.md','README.md','GLOSSARY.md')
$ad = [System.IO.Path]::GetFileName($tam)
if ($beyazListe -contains $ad) { exit 0 }

[Console]::Error.WriteLine("Kokte markdown olusturulamaz: $ad")
[Console]::Error.WriteLine("PROJECT.md bolum 5 - beyaz liste disindaki tum .md dosyalari docs/ altina yazilir.")
exit 2
