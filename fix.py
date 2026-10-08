import re

files = [r'D:\groww sep\Kids Indoor Play Zone & Party Center\index.html', r'D:\groww sep\Kids Indoor Play Zone & Party Center\index2.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add flex flex-col to cards
    content = re.sub(r'class="rounded-2xl bg-white min-w-\[300px\] flex-1 snap-center', 'class="flex flex-col rounded-2xl bg-white min-w-[300px] flex-1 snap-center', content)
    content = re.sub(r'class="rounded-2xl bg-white p-6 shadow-sm transition-all hover:shadow-lg dark:bg-secondary dark:border dark:border-white/10 min-w-\[300px\] flex-1 snap-center', 'class="flex flex-col rounded-2xl bg-white p-6 shadow-sm transition-all hover:shadow-lg dark:bg-secondary dark:border dark:border-white/10 min-w-[300px] flex-1 snap-center', content)
    content = re.sub(r'class="rounded-2xl min-w-\[300px\] flex-1 snap-center', 'class="flex flex-col rounded-2xl min-w-[300px] flex-1 snap-center', content)
    
    # Add mt-auto to avatar wrapper
    content = re.sub(r'<div class="flex items-center gap-3">(\s*<img src="https://i.pravatar.cc)', r'<div class="mt-auto flex items-center gap-3">\1', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
