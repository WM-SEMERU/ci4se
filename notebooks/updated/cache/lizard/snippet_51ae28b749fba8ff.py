def find_comments_by_me(self, access_token, page=1, count=20):
    url = 'https://openapi.youku.com/v2/comments/by_me.json'
    data = {'client_id': self.client_id, 'access_token': access_token,
        'page': page, 'count': count}
    r = requests.post(url, data=data)
    check_error(r)
    return r.json()