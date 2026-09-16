def bridge(filename):
    if not hasattr(settings, 'BASE_DIR'):
        raise Exception('You must provide BASE_DIR in settings for bridge')
    file_path = getattr(settings, 'BUSTERS_FILE', os.path.join('static',
        'busters.json'))
    buster_file = os.path.join(settings.BASE_DIR, file_path)
    fp = file(buster_file, 'r')
    busters_json = json.loads(fp.read())
    fp.close()
    file_hash = busters_json.get('static/%s' % filename)
    path = static(filename)
    return '%s?%s' % (path, file_hash) if file_hash is not None else path