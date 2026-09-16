def comment_vote(self, comment_id, score):
    params = {'score': score}
    return self._get('comments/{0}/votes.json'.format(comment_id), params,
        method='POST', auth=True)