def reverse_toctree(app, doctree, docname):
    if docname == 'changes':
        for node in doctree.traverse():
            if node.tagname == 'toctree' and node.get('glob'):
                node['entries'].reverse()
                break