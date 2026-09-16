def get_git_hash():
    githash = ''
    if os.path.isdir(os.path.join(basedir, '.git')):
        try:
            proc = subprocess.Popen(['git', '-C', basedir, 'rev-parse',
                'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            rev, err = proc.communicate()
            if proc.returncode == 0:
                githash = rev.strip().decode('ascii')
        except OSError:
            pass
    return githash