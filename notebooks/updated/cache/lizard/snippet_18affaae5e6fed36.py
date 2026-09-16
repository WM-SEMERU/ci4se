def scan_posts(self, really=True, ignore_quit=False, quiet=True):
    while self.db.exists('site:lock') and int(self.db.get('site:lock')) != 0:
        self.logger.info('Waiting for DB lock...')
        time.sleep(0.5)
    self.db.incr('site:lock')
    self.logger.info('Lock acquired.')
    self.logger.info('Scanning site...')
    self._site.scan_posts(really, ignore_quit, quiet)
    timeline = []
    for post in self._site.timeline:
        data = [post.source_path, post.folder, post.is_post, post.
            _template_name, post.compiler.name]
        timeline.append(json.dumps(data))
    self.db.delete('site:timeline')
    if timeline:
        self.db.rpush('site:timeline', *timeline)
    self._write_indexlist('posts')
    self._write_indexlist('all_posts')
    self._write_indexlist('pages')
    self.db.incr('site:rev')
    self.db.decr('site:lock')
    self.logger.info('Lock released.')
    self.logger.info('Site scanned.')
    self.reload_site()