def create_named_notebook(fname, context):
    if os.path.exists(fname):
        return
    from nbformat import v4 as nbf
    text = (
        'Welcome to *pyramid_notebook!* Use *File* *>* *Shutdown* to close this.'
        )
    cells = [nbf.new_markdown_cell(text)]
    greeting = context.get('greeting')
    if greeting:
        cells.append(nbf.new_markdown_cell(greeting))
    cells.append(nbf.new_code_cell(''))
    nb = nbf.new_notebook(cells=cells)
    with open(fname, 'w') as f:
        writer = JSONWriter()
        writer.write(nb, f)