async def get_version(self, tp, params):
    tw = TypeWrapper(tp, params)
    if not tw.is_versioned():
        return TypeWrapper.ELEMENTARY_RES
    if not self.version_db.is_versioned(tw):
        tr = await load_uvarint(self.iobj)
        ver = await load_uvarint(self.iobj)
        self.version_db.set_version(tw, tr, ver)
    else:
        tr, ver = self.version_db.get_version(tw)
    obj_id = None if tr == 0 else await load_uvarint(self.iobj)
    self.registry.set_tr(obj_id)
    return ver