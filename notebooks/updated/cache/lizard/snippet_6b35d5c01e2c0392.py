def extract_notebook_metatab(nb_path: Path):
    from metatab.rowgenerators import TextRowGenerator
    import nbformat
    with nb_path.open() as f:
        nb = nbformat.read(f, as_version=4)
    lines = '\n'.join(['Declare: metatab-latest'] + [get_cell_source(nb,
        tag) for tag in ['metadata', 'resources', 'schema']])
    doc = MetapackDoc(TextRowGenerator(lines))
    doc['Root'].get_or_new_term('Root.Title').value = get_cell_source(nb,
        'Title').strip('#').strip()
    doc['Root'].get_or_new_term('Root.Description').value = get_cell_source(nb,
        'Description')
    doc['Documentation'].get_or_new_term('Root.Readme'
        ).value = get_cell_source(nb, 'readme')
    return doc