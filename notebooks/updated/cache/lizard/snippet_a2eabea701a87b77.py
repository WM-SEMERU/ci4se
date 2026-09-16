def _add_members(self, catmembers):
    members = [x for x in catmembers if x['ns'] == 0]
    subcats = [x for x in catmembers if x['ns'] == 14]
    if 'members' in self.data:
        self.data['members'].extend(members)
    else:
        self.data.update({'members': members})
    if subcats:
        if 'subcategories' in self.data:
            self.data['subcategories'].extend(subcats)
        else:
            self.data.update({'subcategories': subcats})