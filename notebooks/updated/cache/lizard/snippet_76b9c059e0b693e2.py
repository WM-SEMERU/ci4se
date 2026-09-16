def bottomup(cls):
    return tuple(unique_everseen(r for r in cls._instances.values() if r.
        direction == 'bottomup'))