def delete_document(self, doc_uri):
    result = self.api_request(doc_uri, method='DELETE')
    return self.__check_success(result)