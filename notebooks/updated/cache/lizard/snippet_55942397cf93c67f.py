def data_size(metadata):
    info = metadata['info']
    if 'length' in info:
        total_size = info['length']
    else:
        total_size = sum([f['length'] for f in info['files']])
    return total_size