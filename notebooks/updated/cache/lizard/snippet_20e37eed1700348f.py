def clean():
    shutil.rmtree(BUILD_PATH, ignore_errors=True)
    shutil.rmtree(os.path.join(SOURCE_PATH, 'reference', 'api'),
        ignore_errors=True)