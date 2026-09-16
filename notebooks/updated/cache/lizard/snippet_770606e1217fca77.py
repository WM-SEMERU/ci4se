def comments(self, update=True):
    if not self._comments:
        if self.count == 0:
            return self._continue_comments(update)
        children = [x for x in self.children if 't1_{0}'.format(x) not in
            self.submission._comments_by_id]
        if not children:
            return None
        data = {'children': ','.join(children), 'link_id': self.submission.
            fullname, 'r': str(self.submission.subreddit)}
        if self.submission._comment_sort:
            data['where'] = self.submission._comment_sort
        url = self.reddit_session.config['morechildren']
        response = self.reddit_session.request_json(url, data=data)
        self._comments = response['data']['things']
        if update:
            for comment in self._comments:
                comment._update_submission(self.submission)
    return self._comments