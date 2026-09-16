def get_outkey(dskey, export_types):
    for exptype in export_types:
        if (dskey, exptype) in export:
            return dskey, exptype