def set_extra_info(self, username, extra_info):
    url = self._get_extra_info_url(username)
    make_request(url, method='PUT', body=extra_info, timeout=self.timeout)