def cleanup_tmpdir(dirname):
    if dirname is not None and os.path.exists(dirname):
        shutil.rmtree(dirname)