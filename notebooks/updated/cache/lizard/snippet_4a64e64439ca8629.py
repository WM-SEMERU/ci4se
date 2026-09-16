def deleted(self, deleted_since, filters=None, params=None):
    return self.tc_requests.deleted(self.api_type, self.api_sub_type,
        deleted_since, owner=self.owner, filters=filters, params=params)