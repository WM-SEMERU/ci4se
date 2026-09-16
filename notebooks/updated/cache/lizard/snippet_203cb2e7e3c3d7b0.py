def can_sequence_objectives(self):
    url_path = construct_url('authorization', bank_id=self._catalog_idstr)
    return self._get_request(url_path)['objectiveHierarchyHints'][
        'canModifyHierarchy']