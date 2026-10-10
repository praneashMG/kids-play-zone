import re

files = [r'D:\groww sep\Kids Indoor Play Zone & Party Center\index.html', r'D:\groww sep\Kids Indoor Play Zone & Party Center\index2.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # ensure the cards have h-full
    content = re.sub(r'(class="flex flex-col rounded-2xl[^"]*?)(")', r'\1 h-full\2', content)
    # remove duplicate h-full if it was added twice
    content = re.sub(r' h-full h-full', r' h-full', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
