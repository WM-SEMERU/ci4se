def search_users(self, username_keyword, limit=10):
    params = {'q': username_keyword, 'limit': limit}
    response = self.get('/users/search', params=params)
    return [GogsUser.from_json(user_json) for user_json in response.json()[
        'data']]