def find_document_type_by_name(self, entity_name, active='Y', match_case=True):
    all_types = self.get_dictionary('Document_Type_DE')
    if match_case:
        filtered = filter(lambda x: x['Active'] == active and x['EntryName'
            ].find(entity_name) >= 0, all_types)
    else:
        token = entity_name.lower()
        filtered = filter(lambda x: x['Active'] == active and x['EntryName'
            ].lower().find(token) >= 0, all_types)
    return filtered