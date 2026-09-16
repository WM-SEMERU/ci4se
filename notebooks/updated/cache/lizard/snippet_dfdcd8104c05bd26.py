def active_joined_organisations(doc):
    if doc.get('type') == 'user' and doc.get('state') != 'deactivated':
        for org_id, state in doc.get('organisations', {}).items():
            if state['state'] == 'deactivated':
                continue
            org = {'_id': org_id}
            yield [doc['_id'], None], org
            try:
                yield [doc['_id'], state['state']], org
            except KeyError:
                pass