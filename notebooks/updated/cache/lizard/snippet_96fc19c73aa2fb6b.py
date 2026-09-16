def download_audit_trail(self, signature_id, document_id):
    connection = Connection(self.token)
    connection.set_url(self.production, self.SIGNS_DOCUMENTS_AUDIT_URL % (
        signature_id, document_id))
    response, headers = connection.file_request()
    if headers['content-type'] == 'application/json':
        return response
    return response