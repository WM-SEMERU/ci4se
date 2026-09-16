def search(self, search_content, search_type, limit=9):
    url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    params = {'s': search_content, 'type': search_type, 'offset': 0, 'sub':
        'false', 'limit': limit}
    result = self.post_request(url, params)
    return result