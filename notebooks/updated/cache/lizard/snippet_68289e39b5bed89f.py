def __get_ws_distance(wstation, latitude, longitude):
    if wstation:
        try:
            wslat = float(wstation[__BRLAT])
            wslon = float(wstation[__BRLON])
            dist = vincenty((latitude, longitude), (wslat, wslon))
            log.debug(
                'calc distance: %s (latitude: %s, longitude: %s, wslat: %s, wslon: %s)'
                , dist, latitude, longitude, wslat, wslon)
            return dist
        except (ValueError, TypeError, KeyError):
            return None
    else:
        return None