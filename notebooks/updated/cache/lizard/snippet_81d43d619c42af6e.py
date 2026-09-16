def _stat(file):
    out = subprocess.check_output(['stat', '-c', '%U %G %a', file]).decode(
        'utf-8')
    return Ownership(*out.strip().split(' '))