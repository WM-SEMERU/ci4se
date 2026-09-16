def create_frames(until=None):
    now = Date.now()
    if until:
        get_orbit(until, now)
    else:
        for body in list_bodies():
            get_orbit(body.name, now)