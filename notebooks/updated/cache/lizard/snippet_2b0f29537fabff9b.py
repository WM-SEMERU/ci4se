def verify_directory(dir):
    tries = 0
    while not os.path.exists(dir):
        try:
            tries += 1
            os.makedirs(dir, compat.octal('0775'))
        except:
            if tries > 5:
                raise