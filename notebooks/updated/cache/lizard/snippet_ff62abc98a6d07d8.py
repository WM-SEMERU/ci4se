def _get_git_tracked_files(rootdir='.'):
    try:
        with open(os.devnull, 'w') as fnull:
            git_files = subprocess.check_output(['git', 'ls-files', rootdir
                ], stderr=fnull)
        return set(git_files.decode('utf-8').split())
    except subprocess.CalledProcessError:
        return None