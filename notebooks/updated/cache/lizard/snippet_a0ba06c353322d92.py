def save_file(data_file, data, dry_run=None):
    if dry_run:
        return
    with open(data_file, 'w', encoding='utf-8') as f:
        if sys.version_info > (3, 0):
            f.write(json.dumps(data))
        else:
            f.write(json.dumps(data).decode('utf-8'))