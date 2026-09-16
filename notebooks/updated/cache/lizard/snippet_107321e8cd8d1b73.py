def upsert(path, value, create_parents=False, **kwargs):
    return _gen_4spec(LCB_SDCMD_DICT_UPSERT, path, value, create_path=
        create_parents, **kwargs)