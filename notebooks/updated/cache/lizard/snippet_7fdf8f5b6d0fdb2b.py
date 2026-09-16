def get_default_contact(self, client=None):
    catalog = api.get_tool('portal_catalog')
    client = client or self.get_client()
    path = api.get_path(self.context)
    if client:
        path = api.get_path(client)
    query = {'portal_type': 'Contact', 'path': {'query': path, 'depth': 1},
        'incactive_state': 'active'}
    contacts = catalog(query)
    if len(contacts) == 1:
        return api.get_object(contacts[0])
    return None