def make_dir(fname):
    file_path, fname = os.path.split(os.path.abspath(fname))
    if not os.path.exists(file_path):
        os.makedirs(file_path)