def doi(self, doi, only_message=True):
    request_url = build_url_endpoint('/'.join([self.ENDPOINT, doi]))
    request_params = {}
    result = self.do_http_request('get', request_url, data=request_params,
        custom_header=str(self.etiquette))
    if result.status_code == 404:
        return
    result = result.json()
    return result['message'] if only_message is True else result