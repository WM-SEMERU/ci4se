def find_package_data():
    l = list()
    for start in ('ambry/support', 'ambry/bundle/default_files'):
        for root, dirs, files in os.walk(start):
            for f in files:
                if f.endswith('.pyc'):
                    continue
                path = os.path.join(root, f).replace('ambry/', '')
                l.append(path)
    return {'ambry': l}