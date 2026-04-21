import re

f = open('index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

# Remove any previous gear-img style blocks
content = re.sub(r'<style>@media[^<]*gear-img[^<]*</style>', '', content)

new_style = """<style>
@media (max-width: 768px) {
  .studio-photo-wrap {
    aspect-ratio: 1 / 1 !important;
  }
  .studio-photo-wrap img {
    object-position: center 55% !important;
  }
}
</style></head>"""

content = content.replace('</head>', new_style)
open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
