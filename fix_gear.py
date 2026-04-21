f = open('index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

new_style = '<style>@media(max-width:768px){.gear-img{aspect-ratio:1/1 !important;object-fit:cover !important;object-position:center 60% !important;width:100% !important;height:auto !important;max-height:100vw !important;display:block !important;}}</style></head>'

# Remove any old gear-img style blocks first
import re
content = re.sub(r'<style>@media\(max-width:768px\)\{\.gear-img\{[^}]+\}[^}]*\}</style>', '', content)

content = content.replace('</head>', new_style)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
