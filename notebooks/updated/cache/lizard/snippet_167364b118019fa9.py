def _read_file(filename):
    with open(filename, 'r') as fid2:
        abem_data_orig = fid2.read()
    fid = StringIO()
    fid.write(abem_data_orig)
    fid.seek(0)
    fid.readline()
    fid.readline()
    file_type = int(fid.readline().strip())
    fid.seek(0)
    return file_type, fid