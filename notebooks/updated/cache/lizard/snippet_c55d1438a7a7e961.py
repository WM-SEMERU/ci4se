def reload_site(self):
    rev = int(self.db.get('site:rev'))
    if rev != self.revision and self.db.exists('site:rev'):
        timeline = self.db.lrange('site:timeline', 0, -1)
        self._timeline = []
        for data in timeline:
            data = json.loads(data.decode('utf-8'))
            self._timeline.append(Post(data[0], self.config, data[1], data[
                2], data[3], self.messages, self._site.compilers[data[4]]))
        self._read_indexlist('posts')
        self._read_indexlist('all_posts')
        self._read_indexlist('pages')
        self.revision = rev
        self.logger.info('Site updated to revision {0}.'.format(rev))
    elif rev == self.revision and self.db.exists('site:rev'):
        pass
    else:
        self.logger.warn('Site needs rescanning.')