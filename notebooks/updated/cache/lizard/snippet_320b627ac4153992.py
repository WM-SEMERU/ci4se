def list_extmods():
    ret = {}
    ext_dir = os.path.join(__opts__['cachedir'], 'extmods')
    mod_types = os.listdir(ext_dir)
    for mod_type in mod_types:
        ret[mod_type] = set()
        for _, _, files in salt.utils.path.os_walk(os.path.join(ext_dir,
            mod_type)):
            for fh_ in files:
                ret[mod_type].add(fh_.split('.')[0])
        ret[mod_type] = list(ret[mod_type])
    return ret