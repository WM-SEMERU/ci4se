def flavor_access_add(flavor_id, project_id, profile=None, **kwargs):
    conn = _auth(profile, **kwargs)
    return conn.flavor_access_add(flavor_id, project_id)