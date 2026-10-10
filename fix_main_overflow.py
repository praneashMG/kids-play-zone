import glob
import re

files = glob.glob(r'D:\groww sep\Kids Indoor Play Zone & Party Center\*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add overflow-x-hidden to <main> and <footer>
    content = re.sub(r'<main class="([^"]*)"', lambda m: '<main class="' + m.group(1) + ' overflow-x-hidden w-full"' if 'overflow-x-hidden' not in m.group(1) else m.group(0), content)
    content = re.sub(r'<footer class="([^"]*)"', lambda m: '<footer class="' + m.group(1) + ' overflow-x-hidden w-full"' if 'overflow-x-hidden' not in m.group(1) else m.group(0), content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
