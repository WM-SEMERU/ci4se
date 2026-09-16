def remove_path(target_path):
    if os.path.isdir(target_path):
        shutil.rmtree(target_path)
    else:
        os.unlink(target_path)