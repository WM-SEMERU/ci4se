def save_version(folder: str):
    fname = os.path.join(folder, C.VERSION_NAME)
    with open(fname, 'w') as out:
        out.write(__version__)