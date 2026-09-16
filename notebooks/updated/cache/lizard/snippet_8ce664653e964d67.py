def InitializeDownload(self, http_request, http=None, client=None):
    self.EnsureUninitialized()
    if http is None and client is None:
        raise exceptions.UserError('Must provide client or http.')
    http = http or client.http
    if client is not None:
        http_request.url = client.FinalizeTransferUrl(http_request.url)
    url = http_request.url
    if self.auto_transfer:
        end_byte = self.__ComputeEndByte(0)
        self.__SetRangeHeader(http_request, 0, end_byte)
        response = http_wrapper.MakeRequest(self.bytes_http or http,
            http_request)
        if response.status_code not in self._ACCEPTABLE_STATUSES:
            raise exceptions.HttpError.FromResponse(response)
        self.__initial_response = response
        self.__SetTotal(response.info)
        url = response.info.get('content-location', response.request_url)
    if client is not None:
        url = client.FinalizeTransferUrl(url)
    self._Initialize(http, url)
    if self.auto_transfer:
        self.StreamInChunks()