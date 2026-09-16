def usable_id(cls, id, datacenter=None):
    try:
        qry_id = int(id)
    except Exception:
        qry_id = cls.from_sysdisk(id) or cls.from_label(id, datacenter)
    if not qry_id:
        msg = 'unknown identifier %s' % id
        cls.error(msg)
    return qry_id