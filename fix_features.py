import re

file_path = r'D:\groww sep\Kids Indoor Play Zone & Party Center\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the flex row container to handle flex-col on mobile
content = re.sub(r'class="flex items-start gap-4 text-center sm:text-left"', 
                 r'class="flex flex-col sm:flex-row items-center sm:items-start gap-4 text-center sm:text-left"', 
                 content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
