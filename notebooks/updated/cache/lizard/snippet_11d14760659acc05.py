def add_comment(self, body, allow_create=False, allow_hashes=True, summary=
    None, hash_create=False):
    if self.thread_id is None:
        self.thread_id = self.lookup_thread_id()
    data = json.dumps({'body': body})
    if self.thread_id is None:
        if allow_create:
            return self.create_thread(body)
        else:
            raise ValueError('Cannot find comment existing comment for %s' %
                self.topic)
    result = requests.post('%s/issues/%s/comments' % (self.base_url, self.
        thread_id), data, auth=(self.user, self.token))
    if result.status_code != 201:
        if result.reason == 'Not Found' and allow_create:
            return self.create_thread(body)
        else:
            raise GitHubAngry('Bad status %s add_comment on %s because %s' %
                (result.status_code, self.topic, result.reason))
    if allow_hashes:
        self.process_hashes(body, allow_create=hash_create)
    return result