def process_hashes(self, body, allow_create=False):
    hash_re = re.compile(self.hashtag_re)
    hashes = hash_re.findall(body)
    done = {self.topic.lower(): True}
    for mention in hashes:
        mention = mention.strip('#')
        if mention.lower() in done:
            continue
        new_thread = self.__class__(owner=self.owner, realm=self.realm,
            topic=mention, user=self.user, token=self.token)
        my_comment = '# Hashtag copy from %s:\n%s' % (self.topic, body)
        new_thread.add_comment(my_comment, allow_create=allow_create,
            allow_hashes=False)
        done[mention.lower()] = True