def cleanup_all(data_home=None):
    removed = 0
    for name, meta in DATASETS.items():
        _, ext = os.path.splitext(meta['url'])
        removed += cleanup_dataset(name, data_home=data_home, ext=ext)
    print('Removed {} fixture objects from {}'.format(removed,
        get_data_home(data_home)))