def most_recent(path, startswith=None, endswith=None):
    candidate_files = []
    for filename in all_files_in_directory(path):
        if startswith and not os.path.basename(filename).startswith(startswith
            ):
            continue
        if endswith and not filename.endswith(endswith):
            continue
        candidate_files.append({'name': filename, 'modtime': os.path.
            getmtime(filename)})
    most_recent = sorted(candidate_files, key=lambda k: k['modtime'],
        reverse=True)
    return most_recent[0]['name'] if most_recent else None