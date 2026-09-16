def read_file_1st_col_only(fname):
    lst = []
    with open(fname, 'r') as f:
        _ = f.readline()
        for line in f:
            lst.append(line.split(',')[0])
    return lst