def get_top_level_links(self, data, many):
    self_link = None
    if many:
        if self.opts.self_url_many:
            self_link = self.generate_url(self.opts.self_url_many)
    elif self.opts.self_url:
        self_link = data.get('links', {}).get('self', None)
    return {'self': self_link}