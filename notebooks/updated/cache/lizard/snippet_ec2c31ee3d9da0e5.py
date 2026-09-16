def forum_post_create(self, topic_id, body):
    params = {'forum_post[topic_id]': topic_id, 'forum_post[body]': body}
    return self._get('forum_posts.json', params, method='POST', auth=True)