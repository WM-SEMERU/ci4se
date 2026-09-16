def tmp_chdir(new_path):
    prev_cwd = os.getcwd()
    os.chdir(new_path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)