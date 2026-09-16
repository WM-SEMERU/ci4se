def delete_item(self, item_uri):
    response = self.api_request(item_uri, method='DELETE')
    return self.__check_success(response)