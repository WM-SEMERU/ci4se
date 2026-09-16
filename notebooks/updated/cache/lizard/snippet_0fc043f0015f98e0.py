def open_window(path):
    if 'pathlib' in modules:
        try:
            call(['open', '-R', str(Path(str(path)))])
        except FileNotFoundError:
            Popen('explorer /select,' + str(Path(str(path))))
    else:
        print(
            'pathlib module must be installed to execute open_window function')