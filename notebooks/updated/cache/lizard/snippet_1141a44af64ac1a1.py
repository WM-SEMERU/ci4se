def use_npm_ci(path):
    with open(os.devnull, 'w') as fnull:
        if (os.path.isfile(os.path.join(path, 'package-lock.json')) or os.
            path.isfile(os.path.join(path, 'npm-shrinkwrap.json'))
            ) and subprocess.call([NPM_BIN, 'ci', '-h'], stdout=fnull,
            stderr=subprocess.STDOUT) == 0:
            return True
    return False