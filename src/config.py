import os

ROOT = os.path.dirname(os.path.dirname(__file__))

SRC = os.path.join(ROOT, 'src')
os.makedirs(SRC, exist_ok=True)

CONTENT = os.path.join(ROOT, 'content')
os.makedirs(CONTENT, exist_ok=True)

TEMPLATES = os.path.join(ROOT, 'templates')
os.makedirs(TEMPLATES, exist_ok=True)

OUTPUT = os.path.join(ROOT, 'docs')
os.makedirs(OUTPUT, exist_ok=True)

POSTS = os.path.join(OUTPUT, 'posts')
os.makedirs(POSTS, exist_ok=True)

IMG = os.path.join(OUTPUT, 'img')
os.makedirs(IMG, exist_ok=True)
