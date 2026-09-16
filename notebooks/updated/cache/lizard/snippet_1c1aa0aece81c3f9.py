def list_attributes(self, name):
    result = self.client.service.getListAttributes(name, self.proxy_id)
    if isinstance(result, list) and len(result) == 1:
        return result[0]
    return result