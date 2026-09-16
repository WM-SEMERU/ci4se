def convert_to_4(self):
    from six.moves.urllib import parse
    if not self.config.has_section('backends'):
        self.config.add_section('backends')
    site = parse.urlparse(self.get('site', default_value=''))
    backend_uri = 'zebra://{username}:{password}@{hostname}'.format(username
        =self.get('username', default_value=''), password=parse.quote(self.
        get('password', default_value=''), safe=''), hostname=site.hostname)
    self.config.set('backends', 'default', backend_uri)
    self.config.remove_option('default', 'username')
    self.config.remove_option('default', 'password')
    self.config.remove_option('default', 'site')
    if not self.config.has_section('default_aliases'):
        self.config.add_section('default_aliases')
    if not self.config.has_section('default_shared_aliases'):
        self.config.add_section('default_shared_aliases')
    if self.config.has_section('wrmap'):
        for alias, mapping in self.config.items('wrmap'):
            self.config.set('default_aliases', alias, mapping)
        self.config.remove_section('wrmap')
    if self.config.has_section('shared_wrmap'):
        for alias, mapping in self.config.items('shared_wrmap'):
            self.config.set('default_shared_aliases', alias, mapping)
        self.config.remove_section('shared_wrmap')