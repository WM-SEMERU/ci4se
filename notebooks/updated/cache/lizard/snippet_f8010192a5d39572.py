def request_doi_status_by_filename(self, file_name, data_type='result'):
    endpoint = self.get_endpoint('submissionDownload')
    params = {'usr': self.api_user, 'pwd': self.api_key, 'file_name':
        file_name, 'type': data_type}
    result = self.do_http_request('get', endpoint, data=params, timeout=10,
        custom_header=str(self.etiquette))
    return result