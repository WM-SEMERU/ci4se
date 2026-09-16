def _remote_folder(dirpath, remotes, syn):
    if dirpath in remotes:
        return remotes[dirpath], remotes
    else:
        parent_dir, cur_dir = os.path.split(dirpath)
        parent_folder, remotes = _remote_folder(parent_dir, remotes, syn)
        s_cur_dir = syn.store(synapseclient.Folder(cur_dir, parent=
            parent_folder))
        remotes[dirpath] = s_cur_dir.id
        return s_cur_dir.id, remotes