def create(self, acl=None):
    parent, name = getParentAndBase(self.path)
    json = {'name': name}
    if acl is not None:
        json['acl'] = acl.to_api_param()
    response = self.client.postJsonHelper(DataDirectory._getUrl(parent),
        json, False)
    if response.status_code != 200:
        raise DataApiError('Directory creation failed: ' + str(response.
            content))