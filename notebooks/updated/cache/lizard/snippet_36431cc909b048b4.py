def usable_id(cls, id):
    try:
        qry_id = cls.from_name(id)
        if not qry_id:
            qry_id = int(id)
    except DuplicateResults as exc:
        cls.error(exc.errors)
    except Exception:
        qry_id = None
    if not qry_id:
        msg = 'unknown identifier %s' % id
        cls.error(msg)
    return qry_id