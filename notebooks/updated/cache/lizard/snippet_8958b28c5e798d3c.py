def get_metadata():
    misc_path = pkg_resources.resource_filename('hwrt', 'misc/')
    wm_symbols = os.path.join(misc_path, 'wm_symbols.csv')
    wm_tags = os.path.join(misc_path, 'wm_tags.csv')
    wm_tags2symbols = os.path.join(misc_path, 'wm_tags2symbols.csv')
    return {'symbols': read_csv(wm_symbols), 'tags': read_csv(wm_tags),
        'tags2symbols': read_csv(wm_tags2symbols)}