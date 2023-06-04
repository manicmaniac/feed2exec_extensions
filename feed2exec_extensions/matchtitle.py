import re

def filter(*args, feed=None, item=None, **kwargs):
    item['skip'] = re.search(' '.join(args), item.get('title', '')) is None
