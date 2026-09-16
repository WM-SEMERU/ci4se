def get_dict(cls):
    mdt = cls.get()
    if not mdt:
        return {}
    return conspectus.subs_by_mdt.get(mdt, {})