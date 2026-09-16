def follow_redirections(self, request):
    log.debug(LOG_CHECK, 'follow all redirections')
    if self.is_redirect():
        self.aggregate.plugin_manager.run_connection_plugins(self)
    response = None
    for response in self.get_redirects(request):
        newurl = response.url
        log.debug(LOG_CHECK, 'Redirected to %r', newurl)
        self.aliases.append(newurl)
        self.add_info(_("Redirected to `%(url)s'.") % {'url': newurl})
        self.extern = None
        self.set_extern(newurl)
        self.urlparts = strformat.url_unicode_split(newurl)
        self.build_url_parts()
        self.url_connection = response
        self.headers = response.headers
        self.url = urlutil.urlunsplit(self.urlparts)
        self.scheme = self.urlparts[0].lower()
        self._add_ssl_info()
        self._add_response_info()
        if self.is_redirect():
            self.aggregate.plugin_manager.run_connection_plugins(self)