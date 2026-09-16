def get_home_position(boatd=None):
    if boatd is None:
        boatd = Boatd()
    content = boatd.get('/waypoints')
    home = content.get('home', None)
    if home is not None:
        lat, lon = home
        return Point(lat, lon)
    else:
        return None