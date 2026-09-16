def check():
    dist_path = Path(DIST_PATH)
    if not dist_path.exists() or not list(dist_path.glob('*')):
        print("No distribution files found. Please run 'build' command first")
        return
    subprocess.check_call(['twine', 'check', 'dist/*'])