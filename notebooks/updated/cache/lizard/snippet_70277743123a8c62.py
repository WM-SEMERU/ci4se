def _ep_to_kv(entrypoint):
    cls = entrypoint.load()
    cls.name = entrypoint.name
    return entrypoint.name, cls