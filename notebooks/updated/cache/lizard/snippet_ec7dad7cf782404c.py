def decompress_file(filepath):
    toks = filepath.split('.')
    file_ext = toks[-1].upper()
    from monty.io import zopen
    if file_ext in ['BZ2', 'GZ', 'Z']:
        with open('.'.join(toks[0:-1]), 'wb') as f_out, zopen(filepath, 'rb'
            ) as f_in:
            f_out.writelines(f_in)
        os.remove(filepath)