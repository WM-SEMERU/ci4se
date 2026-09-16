def safe_rmtree(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory, True)