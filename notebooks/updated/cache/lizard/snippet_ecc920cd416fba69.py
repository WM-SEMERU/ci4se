def upload_file_mp(self, container, src_file_path, dst_name=None,
    content_type=None):
    if not os.path.exists(src_file_path):
        raise RuntimeError('file not found: ' + src_file_path)
    if not dst_name:
        dst_name = os.path.basename(src_file_path)
    if not content_type:
        content_type = 'application/octet.stream'
    url = self.make_url(container, None, None)
    headers = self._base_headers
    with open(src_file_path, 'rb') as up_file:
        files = {'file': (dst_name, up_file, content_type)}
        try:
            rsp = requests.post(url, headers=headers, files=files, timeout=
                self._timeout)
        except requests.exceptions.ConnectionError as e:
            RestHttp._raise_conn_error(e)
    return self._handle_response(rsp)