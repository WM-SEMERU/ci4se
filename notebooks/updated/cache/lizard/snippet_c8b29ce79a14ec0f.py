def get_record_status(recid):
    collections_with_rounds = CFG_WEBCOMMENT_ROUND_DATAFIELD.keys()
    commenting_round = ''
    for collection in collections_with_rounds:
        if recid in get_collection_reclist(collection):
            commenting_rounds = get_fieldvalues(recid,
                CFG_WEBCOMMENT_ROUND_DATAFIELD.get(collection, ''))
            if commenting_rounds:
                commenting_round = commenting_rounds[0]
            break
    collections_with_restrictions = CFG_WEBCOMMENT_RESTRICTION_DATAFIELD.keys()
    restriction = ''
    for collection in collections_with_restrictions:
        if recid in get_collection_reclist(collection):
            restrictions = get_fieldvalues(recid,
                CFG_WEBCOMMENT_RESTRICTION_DATAFIELD.get(collection, ''))
            if restrictions:
                restriction = restrictions[0]
            break
    return restriction, commenting_round