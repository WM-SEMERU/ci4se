def can_assign_requisites(self):
    url_path = construct_url('authorization', bank_id=self._catalog_idstr)
    return self._get_request(url_path)['objectiveRequisiteHints']['canAssign']