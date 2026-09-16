def __update_kind(uid, kind):
    entry = TabPost.update(kind=kind).where(TabPost.uid == uid)
    entry.execute()
    return True