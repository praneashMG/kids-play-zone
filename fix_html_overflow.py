import glob
import re

files = glob.glob(r'D:\groww sep\Kids Indoor Play Zone & Party Center\*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add overflow-x-hidden to html if not already there
    if 'html' in content and 'overflow-x-hidden' not in content.split('<head>')[0]:
        content = re.sub(r'<html([^>]*)>', lambda m: '<html' + m.group(1) + ' class="overflow-x-hidden"' if 'class="' not in m.group(1) else '<html' + m.group(1).replace('class="', 'class="overflow-x-hidden '), content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
