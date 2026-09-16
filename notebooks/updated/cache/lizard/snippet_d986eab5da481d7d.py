def load_site(self, purge_first=False, full=False, modified_after=None,
    type=None, status=None, batch_size=None):
    self.purge_first = purge_first
    self.full = full
    self.modified_after = modified_after
    self.batch_size = batch_size or 100
    if type is None:
        type = 'all'
    if status is None:
        status = 'publish'
    if type in ['all', 'ref_data']:
        self.load_categories()
        self.load_tags()
        self.load_authors()
        self.load_media()
    if type in ['all', 'attachment', 'post', 'page']:
        self.get_ref_data_map()
    if type == 'all':
        for post_type in ['attachment', 'post', 'page']:
            self.load_posts(post_type=post_type, status=status)
    elif type in ['attachment', 'post', 'page']:
        self.load_posts(post_type=type, status=status)