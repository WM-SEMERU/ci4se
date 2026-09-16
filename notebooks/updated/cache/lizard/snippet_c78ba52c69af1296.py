def get_design_document(self, ddoc_id):
    ddoc = DesignDocument(self, ddoc_id)
    try:
        ddoc.fetch()
    except HTTPError as error:
        if error.response.status_code != 404:
            raise
    return ddoc