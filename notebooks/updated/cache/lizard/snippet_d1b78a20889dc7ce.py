def comment_delete(self, comment_id):
    return self._get('comments/{0}.json'.format(comment_id), method=
        'DELETE', auth=True)