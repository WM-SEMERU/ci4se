def format_repo_status(repo):
    commit = repo.commit()
    return {'name': os.path.basename(repo.working_dir), 'commit': commit.
        hexsha, 'timestamp': datetime.fromtimestamp(commit.committed_date).
        isoformat()}