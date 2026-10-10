import glob
import re

files = glob.glob(r'D:\groww sep\Kids Indoor Play Zone & Party Center\*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove overflow-x-hidden from html
    content = re.sub(r'<html([^>]*) class="([^"]*)overflow-x-hidden([^"]*)"', r'<html\1 class="\2\3"', content)
    content = re.sub(r'<html([^>]*) class="\s+"', r'<html\1', content) # clean up empty class if any
    
    # Remove overflow-x-hidden from body
    content = re.sub(r'<body([^>]*) class="([^"]*)overflow-x-hidden([^"]*)"', r'<body\1 class="\2\3"', content)

    # Make sure we clean up any double spaces or dangling spaces
    content = content.replace('  ', ' ').replace(' >', '>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
