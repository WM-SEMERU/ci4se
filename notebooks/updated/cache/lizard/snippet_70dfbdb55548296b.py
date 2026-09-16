def unpack(table, field, newfields=None, include_original=False, missing=None):
    return UnpackView(table, field, newfields=newfields, include_original=
        include_original, missing=missing)