def listflat(path, ext=None):
    if os.path.isdir(path):
        if ext:
            if ext == 'tif' or ext == 'tiff':
                files = glob.glob(os.path.join(path, '*.tif'))
                files = files + glob.glob(os.path.join(path, '*.tiff'))
            else:
                files = glob.glob(os.path.join(path, '*.' + ext))
        else:
            files = [os.path.join(path, fname) for fname in os.listdir(path)]
    else:
        files = glob.glob(path)
    files = [fpath for fpath in files if not isinstance(fpath, list) and 
        not os.path.isdir(fpath)]
    return sorted(files)