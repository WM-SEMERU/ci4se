def create_id2amendment_info(path, tag):
    d = {}
    for triple in os.walk(path):
        root, files = triple[0], triple[2]
        for filename in files:
            if filename.endswith('.json'):
                amendment_id = n = filename[:-5]
                d[amendment_id] = tag, root, os.path.join(root, filename)
    return d