def update_name(self, force=False, create_term=False, report_unchanged=True):
    updates = []
    self.ensure_identifier()
    name_term = self.find_first('Root.Name')
    if not name_term:
        if create_term:
            name_term = self['Root'].new_term('Root.Name', '')
        else:
            updates.append("No Root.Name, can't update name")
            return updates
    orig_name = name_term.value
    identifier = self.get_value('Root.Identifier')
    datasetname = self.get_value('Root.Dataset')
    if datasetname:
        name = self._generate_identity_name()
        if name != orig_name or force:
            name_term.value = name
            updates.append('Changed Name')
        elif report_unchanged:
            updates.append('Name did not change')
    elif not orig_name:
        if not identifier:
            updates.append(
                'Failed to find DatasetName term or Identity term. Giving up')
        else:
            updates.append('Setting the name to the identifier')
            name_term.value = identifier
    elif orig_name == identifier:
        if report_unchanged:
            updates.append('Name did not change')
    else:
        updates.append("No Root.Dataset, so can't update the name")
    return updates