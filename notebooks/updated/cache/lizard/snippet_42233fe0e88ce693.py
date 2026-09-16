def comment_update(self, comment_id, body):
    params = {'comment[body]': body}
    return self._get('comments/{0}.json'.format(comment_id), params, 'PUT',
        auth=True)