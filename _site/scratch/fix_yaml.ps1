$files = Get-ChildItem -Path "lorebook/story" -Recurse -Filter *.md
foreach ($file in $files) {
    $content = Get-Content $file.FullName
    $newContent = @()
    foreach ($line in $content) {
        if ($line -match '^title: "(.*)", "(.*)"$') {
            $line = 'title: "' + $Matches[1] + ', ' + $Matches[2] + '"'
        }
        $newContent += $line
    }
    $newContent | Set-Content $file.FullName
}
