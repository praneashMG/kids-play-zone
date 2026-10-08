import re

file_path = r'D:\groww sep\Kids Indoor Play Zone & Party Center\pricing.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the outer card class to include flex flex-col h-full
content = re.sub(r'class="group overflow-hidden rounded-2xl bg-gray-50 shadow-sm transition-all hover:shadow-xl hover:-translate-y-1 dark:bg-white/5 dark:border dark:border-white/10(\s*sm:col-span-2 lg:col-span-1)?"', 
                 r'class="group overflow-hidden rounded-2xl bg-gray-50 shadow-sm transition-all hover:shadow-xl hover:-translate-y-1 dark:bg-white/5 dark:border dark:border-white/10 flex flex-col h-full\1"', 
                 content)

# 2. Update the inner container to include flex flex-col flex-1
content = re.sub(r'<div class="p-6 text-center">', r'<div class="p-6 text-center flex flex-col flex-1">', content)

# 3. Update the price to have mt-auto
content = re.sub(r'<p class="text-2xl font-extrabold text-accent">', r'<p class="text-2xl font-extrabold text-accent mt-auto">', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
