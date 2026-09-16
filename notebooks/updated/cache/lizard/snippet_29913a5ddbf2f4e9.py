def render_files(self, root=None):
    if root is None:
        tmp = os.environ.get('TMP')
        root = sys.path[1 if tmp and tmp in sys.path else 0]
    items = []
    for filename in os.listdir(root):
        f, ext = os.path.splitext(filename)
        if ext in ['.py', '.enaml']:
            items.append(FILE_TMPL.format(name=filename, id=filename))
    return ''.join(items)