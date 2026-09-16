def joined_organisations(doc):
    if doc.get('type') == 'user':
        for org_id, state in doc.get('organisations', {}).items():
            org = {'_id': org_id}
            yield [doc['_id'], None], org
            try:
                yield [doc['_id'], state['state']], org
            except KeyError:
                pass