def chmod(scope, filename, mode):
    for file in filename:
        os.chmod(file, mode[0])
    return True