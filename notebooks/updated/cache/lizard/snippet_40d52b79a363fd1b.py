def get_type_data(self, name):
    try:
        return {'authority': 'DLKIT', 'namespace':
            'relationship.Relationship', 'identifier': name.lower(),
            'domain': 'Generic Types', 'display_name': name.title() +
            ' Type', 'display_label': name.title(), 'description': 'The ' +
            name.title() + ' Type.'}
    except IndexError:
        raise NotFound('RelationshipType: ' + name.title())