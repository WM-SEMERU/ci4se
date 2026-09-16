def get_allowed(allow, disallow):
    if allow is None and disallow is None:
        return SUMO_VEHICLE_CLASSES
    elif disallow is None:
        return allow.split()
    else:
        disallow = disallow.split()
        return tuple([c for c in SUMO_VEHICLE_CLASSES if c not in disallow])