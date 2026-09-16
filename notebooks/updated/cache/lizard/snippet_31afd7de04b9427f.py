def sort_csv(in_file):
    out_file = '%s.sort' % in_file
    if not (os.path.exists(out_file) and os.path.getsize(out_file) > 0):
        cl = ['sort', '-k', '1,1', in_file]
        with open(out_file, 'w') as out_handle:
            child = subprocess.Popen(cl, stdout=out_handle)
            child.wait()
    return out_file