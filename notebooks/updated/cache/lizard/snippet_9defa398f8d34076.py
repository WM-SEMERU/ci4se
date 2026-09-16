def contributor_group(self):
    items = listify(chained_get(self._head, ['source', 'contributor-group'],
        []))
    out = []
    fields = 'given_name initials surname indexed_name role'
    pers = namedtuple('Contributor', fields)
    for item in items:
        entry = item.get('contributor', {})
        new = pers(indexed_name=entry.get('ce:indexed-name'), role=entry.
            get('@role'), surname=entry.get('ce:surname'), given_name=entry
            .get('ce:given-name'), initials=entry.get('ce:initials'))
        out.append(new)
    return out or None