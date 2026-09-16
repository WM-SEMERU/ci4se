def dedupe_by(things, key=None):
    if not key:
        key = hash
    index = {key(thing): thing for thing in things}
    return index.values()