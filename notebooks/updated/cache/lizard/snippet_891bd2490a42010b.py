def read_committed_file(gitref, filename):
    repo = Repo()
    commitobj = repo.commit(gitref)
    blob = commitobj.tree[_delta_dir() + filename]
    return blob.data_stream.read()