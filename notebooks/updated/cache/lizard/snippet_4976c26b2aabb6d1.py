def set_id_in_fkeys(cls, payload):
    for key in payload:
        val = payload[key]
        if not val:
            continue
        if key.endswith('_id'):
            model = getattr(THIS_MODULE, cls.FKEY_MAP[key])
            rec_id = model.replace_name_with_id(name=val)
            payload[key] = rec_id
        elif key.endswith('_ids'):
            model = getattr(THIS_MODULE, cls.FKEY_MAP[key])
            rec_ids = []
            for v in val:
                rec_id = model.replace_name_with_id(name=v)
                rec_ids.append(rec_id)
            payload[key] = rec_ids
    return payload