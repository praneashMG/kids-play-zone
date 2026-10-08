import re

files = [r'D:\groww sep\Kids Indoor Play Zone & Party Center\admin-dashboard.html', r'D:\groww sep\Kids Indoor Play Zone & Party Center\user-dashboard.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the hidden class on the logo text
    content = re.sub(r'<div class="leading-tight hidden sm:block">(\s*<span class="block text-lg sm:text-xl font-medium tracking-tight text-a">Kids Play Zone</span>)', 
                     r'<div class="leading-tight">\1', 
                     content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
