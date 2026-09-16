def create(self, name, **params):
    if not isinstance(name, six.string_types):
        raise ValueError('Invalid role name: %s' % str(name))
    name = name.lower()
    self.post(name=name, **params)
    response = self.get(name)
    entry = _load_atom(response, XNAME_ENTRY).entry
    state = _parse_atom_entry(entry)
    entity = self.item(self.service, urllib.parse.unquote(state.links.
        alternate), state=state)
    return entity