def diagnose_repo_nexml2json(shard):
    with shard._index_lock:
        fp = next(iter(shard.study_index.values()))[2]
    with codecs.open(fp, mode='r', encoding='utf-8') as fo:
        fj = json.load(fo)
        from peyotl.nexson_syntax import detect_nexson_version
        return detect_nexson_version(fj)