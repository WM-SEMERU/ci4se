def get_vcs_info(path):
    for info in SUPPORTED:
        vcs_path = osp.join(path, info['rootdir'])
        if osp.isdir(vcs_path):
            return info