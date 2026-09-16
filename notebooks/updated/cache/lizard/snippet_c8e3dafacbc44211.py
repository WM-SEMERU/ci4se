def update_metatab(self, doc, resources):
    if not 'Documentation' in doc:
        doc.new_section('Documentation')
    ds = doc['Documentation']
    if not 'Name' in ds.args:
        ds.add_arg('Name', prepend=True)
    ds.new_term('Root.Documentation', 'docs/notebook.html', name=
        'notebook.html', title='Jupyter Notebook (HTML)')
    for name, data in resources.get('outputs', {}).items():
        if name == 'documentation.html':
            ds.new_term('Root.Documentation', 'docs/' + name, name=name,
                title='Primary Documentation (HTML)')
        elif name == 'html_basic_body.html':
            pass
        elif name.endswith('.html'):
            ds.new_term('Root.Documentation', 'docs/' + name, name=name,
                title='Documentation (HTML)')
        elif name.endswith('.md'):
            ds.new_term('Root.Documentation', 'docs/' + name, name=name,
                title='Documentation (Markdown)')
        elif name.endswith('.pdf'):
            ds.new_term('Root.Documentation', 'docs/' + name, name=name,
                title='Documentation (PDF)')
        elif name.endswith('.png'):
            ds.new_term('Root.Image', 'docs/' + name, name=name, title=
                'Image for HTML Documentation')
        else:
            pass