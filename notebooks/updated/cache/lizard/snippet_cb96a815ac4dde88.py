def can_create_repository_with_record_types(self, repository_record_types=None
    ):
    url_path = construct_url('authorization', bank_id=self._catalog_idstr)
    return self._get_request(url_path)['objectiveBankHints']['canCreate']