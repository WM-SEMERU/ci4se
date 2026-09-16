def clean_cell_meta(self, meta):
    for k, v in DEFAULT_CELL_METADATA.items():
        if meta.get(k, None) == v:
            meta.pop(k, None)
    return meta