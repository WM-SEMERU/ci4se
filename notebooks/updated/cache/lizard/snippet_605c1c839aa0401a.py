def run_cmd_if_file_missing(cmd, fname, out=os.path.devnull, err=os.path.
    devnull):
    if fname is None or not os.path.exists(fname):
        run_cmd(cmd, out, err)
        return True
    else:
        return False