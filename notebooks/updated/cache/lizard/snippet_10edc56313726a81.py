def suspend(instance_id, profile=None, **kwargs):
    conn = _auth(profile, **kwargs)
    return conn.suspend(instance_id)