def write_file(fname_parts, content):
    fname_parts = [str(part) for part in fname_parts]
    if len(fname_parts) > 1:
        try:
            os.makedirs(os.path.join(*fname_parts[:-1]))
        except OSError:
            pass
    fhandle = open(os.path.join(*fname_parts), 'w')
    fhandle.write(content)
    fhandle.close()