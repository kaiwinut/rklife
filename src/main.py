import os
from datetime import date, datetime
from re import TEMPLATE
from jinja2 import Environment, PackageLoader
from markdown2 import markdown
from config import *

def sorted_by_time(posts, *, reverse=True):
    return sorted(posts, key=lambda post: datetime.strptime(posts[post].metadata['date'], '%Y-%m-%d'), reverse=reverse)

posts = {}

for post_file_name in os.listdir(CONTENT):
    path = os.path.join(CONTENT, post_file_name)

    with open(path, 'r') as f:
        posts[post_file_name] = markdown(f.read(), extras=['metadata'])

posts = {
    file: posts[file] for file in sorted_by_time(posts)
}

env = Environment(loader=PackageLoader('main', TEMPLATES))
index_tmp = env.get_template('index.html')
post_tmp = env.get_template('post.html')

metadatas = [posts[file].metadata for file in posts]
index_html = index_tmp.render(posts=metadatas, tags=[meta['tags'] for meta in metadatas])

with open(os.path.join(OUTPUT, 'index.html'), 'w') as f:
    f.write(index_html)

for file in posts:
    metadata = posts[file].metadata
    data = {
        'content': posts[file],
        'title': metadata['title'],
        'date': metadata['date'],
    }
    post_html = post_tmp.render(post=data)
    output_path = os.path.join(POSTS, f'{metadata["slug"]}.html')
    with open(output_path, 'w') as f:
        f.write(post_html)