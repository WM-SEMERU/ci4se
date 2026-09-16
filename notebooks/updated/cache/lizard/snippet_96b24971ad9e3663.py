def listdir(self, url):
    params = self._split_url(url)
    block_blob_service = self._block_blob_service(account_name=params[
        'account'], sas_token=params['sas_token'])
    blobs = block_blob_service.list_blobs(params['container'])
    return blobs