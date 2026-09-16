def get_raw_files(raw_dir, data_source):
    raw_files = {'inputs': [], 'targets': []}
    for d in data_source:
        input_file, target_file = download_and_extract(raw_dir, d['url'], d
            ['input'], d['target'])
        raw_files['inputs'].append(input_file)
        raw_files['targets'].append(target_file)
    return raw_files