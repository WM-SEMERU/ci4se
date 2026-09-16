def generate_rss(self, path='rss.xml', only_excerpt=True, https=False):
    feed = russell.feed.get_rss_feed(self, only_excerpt=only_excerpt, https
        =https)
    feed.rss_file(self._get_dist_path(path))