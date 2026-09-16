def verify_gmt_integrity(gmt):
    set_ids = [d[SET_IDENTIFIER_FIELD] for d in gmt]
    assert len(set(set_ids)) == len(set_ids
        ), 'Set identifiers should be unique. set_ids: {}'.format(set_ids)