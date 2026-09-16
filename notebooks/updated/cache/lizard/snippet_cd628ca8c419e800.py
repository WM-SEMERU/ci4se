def id_to_extended_id(item_id, item_class):
    out = ID_PREFIX[item_class]
    if out:
        out += item_id
    return out