def parse_segdict_key(self, key):
    splt = key.split(':')
    if len(splt) == 2:
        return splt[0], splt[1]
    else:
        err_msg = "Key should be of the format 'ifo:name', got %s." % (key,)
        raise ValueError(err_msg)