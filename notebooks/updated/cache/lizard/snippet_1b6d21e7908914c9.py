def get_objective_bank(self):
    url_path = construct_url('objective_banks', bank_id=self._catalog_idstr)
    return objects.ObjectiveBank(self._get_request(url_path))