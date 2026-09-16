def from_git_rev_read(path):
    if ':' not in path:
        raise ValueError('Path identifier must start with a revision hash.')
    cmd = 'git', 'show', '-t', path
    try:
        return subprocess.check_output(cmd).rstrip().decode('utf-8')
    except subprocess.CalledProcessError:
        raise ValueError