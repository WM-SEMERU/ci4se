def placeFiles(ftp, path):
    for name in os.listdir(path):
        if (name != 'config.py' and name != 'config.pyc' and name !=
            'templates' and name != 'content'):
            localpath = os.path.join(path, name)
            if os.path.isfile(localpath):
                print('STOR', name, localpath)
                ftp.storbinary('STOR ' + name, open(localpath, 'rb'))
            elif os.path.isdir(localpath):
                print('MKD', name)
                try:
                    ftp.mkd(name)
                except error_perm as e:
                    if not e.args[0].startswith('550'):
                        raise
                print('CWD', name)
                ftp.cwd(name)
                placeFiles(ftp, localpath)
                print('CWD', '..')
                ftp.cwd('..')