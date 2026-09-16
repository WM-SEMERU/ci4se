def get_reference_data(data_dir=None):
    data_dir = fix_data_dir(data_dir)
    reffile_path = os.path.join(data_dir, 'REFERENCES.json')
    return fileio.read_references(reffile_path)