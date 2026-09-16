def is_unit_upgrading_set():
    try:
        with unitdata.HookData()() as t:
            kv = t[0]
            return not not kv.get('unit-upgrading')
    except Exception:
        return False