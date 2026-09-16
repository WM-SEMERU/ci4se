def extract_log(rpath, extract=simple_attributes):
    m_repo = git.Repo(rpath)
    count = 0
    m_commits = m_repo.iter_commits()
    for commit in m_commits:
        count += 1
    with tqdm.tqdm(total=count) as pbar:
        m_commits = m_repo.iter_commits()
        update_interval = max(min(count // 100, 100), 5)
        index = 0
        buffer = []
        while True:
            try:
                next_commit = next(m_commits)
                buffer.append(make_object_dict(next_commit, extract))
                index += 1
                if index % update_interval == 0:
                    pbar.update(update_interval)
            except StopIteration:
                break
    return pd.DataFrame(buffer)