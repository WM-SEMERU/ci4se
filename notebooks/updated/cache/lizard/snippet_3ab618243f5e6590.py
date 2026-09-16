def temporary_directory():
    dir_name = tempfile.mkdtemp()
    yield dir_name
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)