def merge_split(*paths):
    filtered_paths = filter(None, paths)
    return [p for p in ':'.join(filtered_paths).split(':') if p]