def comment_create(self, post_id, comment_body, anonymous=None):
    params = {'comment[post_id]': post_id, 'comment[body]': comment_body,
        'comment[anonymous]': anonymous}
    return self._get('comment/create', params, method='POST')