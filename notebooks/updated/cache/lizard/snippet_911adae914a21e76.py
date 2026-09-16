def forum_post_update(self, topic_id, body):
    params = {'forum_post[body]': body}
    return self._get('forum_posts/{0}.json'.format(topic_id), params,
        method='PUT', auth=True)