def add_files_to_git_repository(base_dir, files, description):
    if not os.path.isdir(base_dir):
        printOut(
            'Output path is not a directory, cannot add files to git repository.'
            )
        return
    gitRoot = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], cwd
        =base_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = gitRoot.communicate()[0]
    if gitRoot.returncode != 0:
        printOut(
            'Cannot commit results to repository: git rev-parse failed, perhaps output path is not a git directory?'
            )
        return
    gitRootDir = decode_to_string(stdout).splitlines()[0]
    gitStatus = subprocess.Popen(['git', 'status', '--porcelain',
        '--untracked-files=no'], cwd=gitRootDir, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    stdout, stderr = gitStatus.communicate()
    if gitStatus.returncode != 0:
        printOut('Git status failed! Output was:\n' + decode_to_string(stderr))
        return
    if stdout:
        printOut('Git repository has local changes, not commiting results.')
        return
    files = [os.path.realpath(file) for file in files]
    gitAdd = subprocess.Popen(['git', 'add', '--force', '--'] + files, cwd=
        gitRootDir)
    if gitAdd.wait() != 0:
        printOut('Git add failed, will not commit results!')
        return
    printOut('Committing results files to git repository in ' + gitRootDir)
    gitCommit = subprocess.Popen(['git', 'commit', '--file=-', '--quiet'],
        cwd=gitRootDir, stdin=subprocess.PIPE)
    gitCommit.communicate(description.encode('UTF-8'))
    if gitCommit.returncode != 0:
        printOut('Git commit failed!')
        return