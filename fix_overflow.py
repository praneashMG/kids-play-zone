import glob
import re

files = glob.glob(r'D:\groww sep\Kids Indoor Play Zone & Party Center\*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add overflow-x-hidden to body if not already there
    if 'overflow-x-hidden' not in content:
        content = re.sub(r'<body class="(.*?)"', r'<body class="\1 overflow-x-hidden"', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
