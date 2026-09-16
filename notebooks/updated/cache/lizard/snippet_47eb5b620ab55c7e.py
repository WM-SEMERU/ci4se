def get_image_list(self, page=1, per_page=20):
    url = self.api_url + '/api/images'
    params = {'page': page, 'per_page': per_page}
    response = self._request_url(url, 'get', params=params,
        with_access_token=True)
    headers, result = self._parse_and_check(response)
    images = ImageList.from_list(result)
    images.set_attributes_from_headers(headers)
    return images