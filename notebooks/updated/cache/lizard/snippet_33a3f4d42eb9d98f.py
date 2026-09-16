def get_label_map(opts):
    result = {}
    try:
        for entry in os.scandir(diskdir):
            if entry.name.startswith('.'):
                continue
            if islink(entry.path):
                target = os.readlink(entry.path)
            else:
                target = entry.path
            result[target] = entry.name
        if opts.debug:
            print('\n\nlabel_map:', result)
    except FileNotFoundError:
        pass
    return result