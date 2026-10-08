import re

files = [r'D:\groww sep\Kids Indoor Play Zone & Party Center\signup.html', r'D:\groww sep\Kids Indoor Play Zone & Party Center\login.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add mt-10 to the mobile logo to avoid overlap with fixed buttons
    content = re.sub(r'<div class="md:hidden text-center mb-6">', r'<div class="md:hidden text-center mb-4 mt-8">', content)
    
    # Reduce margins to make content tighter on mobile
    content = re.sub(r'<div class="mb-5 text-center">', r'<div class="mb-3 sm:mb-5 text-center">', content)
    content = re.sub(r'<div class="flex justify-center gap-3.5 mb-5">', r'<div class="flex justify-center gap-3.5 mb-3 sm:mb-5">', content)
    content = re.sub(r'<div class="flex items-center gap-3 mb-4">', r'<div class="flex items-center gap-3 mb-3 sm:mb-4">', content)
    
    # Reduce input padding slightly
    content = re.sub(r'py-2\.5', r'py-2 sm:py-2.5', content)
    
    # Adjust spacing in form
    content = re.sub(r'space-y-3 sm:space-y-3\.5', r'space-y-2 sm:space-y-3.5', content)
    
    # Adjust outer padding
    content = re.sub(r'p-4 sm:p-6 lg:p-10', r'p-4 sm:p-6 lg:p-10', content) # keep outer padding same, but the mt-8 above handles the top

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
