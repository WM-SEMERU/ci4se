def _get_file_list(load):
    if 'env' in load:
        load.pop('env')
    if 'saltenv' not in load or load['saltenv'] not in envs():
        return []
    ret = set()
    for repo in init():
        repo['repo'].open()
        ref = _get_ref(repo, load['saltenv'])
        if ref:
            manifest = repo['repo'].manifest(rev=ref[1])
            for tup in manifest:
                relpath = os.path.relpath(tup[4], repo['root'])
                if not relpath.startswith('../'):
                    ret.add(os.path.join(repo['mountpoint'], relpath))
        repo['repo'].close()
    return sorted(ret)