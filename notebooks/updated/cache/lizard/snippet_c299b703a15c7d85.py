def load_spitzer_catalog(show_progress=False):
    path = get_path('spitzer_example_catalog.xml', location='remote',
        show_progress=show_progress)
    table = Table.read(path)
    return table