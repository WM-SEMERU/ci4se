def fetch_changes(repo_path, up_commit='master'):
    last_up_commit = None
    prevcwd = os.getcwd()
    try:
        gitexe = 'git'
        os.chdir(repo_path)
        old_sources_timestamp = sources_latest_timestamp('.')
        shell_command([gitexe, 'pull'])
        last_up_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        shell_command([gitexe, 'checkout', up_commit])
        up_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
        new_sources_timestamp = sources_latest_timestamp('.')
        if old_sources_timestamp < new_sources_timestamp:
            with open('.timestamp', 'w') as up_commit_file:
                up_commit_file.write(up_commit)
    finally:
        os.chdir(prevcwd)
    return last_up_commit, up_commit