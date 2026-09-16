def insert_entry(self, entry, taxids):
    entry_dict = entry.attrib
    entry_dict['created'] = datetime.strptime(entry_dict['created'], '%Y-%m-%d'
        )
    entry_dict['modified'] = datetime.strptime(entry_dict['modified'],
        '%Y-%m-%d')
    taxid = self.get_taxid(entry)
    if taxids is None or taxid in taxids:
        entry_dict = self.update_entry_dict(entry, entry_dict, taxid)
        entry_obj = models.Entry(**entry_dict)
        del entry_dict
        self.session.add(entry_obj)