def check_status(self):
    log = logging.getLogger('%s.%s' % (self.log_name, inspect.stack()[0][3]))
    log.setLevel(self.log_level)
    if self.url:
        return True
    try:
        result = requests.get(self.ext_url)
        self.url = self.ext_url
        return True
    except requests.exceptions.ConnectionError:
        pass
    try:
        result = requests.get(self.local_url)
        log.warning("Url '%s' not connecting. Using local_url '%s'" % (self
            .ext_url, self.local_url))
        self.url = self.local_url
        return True
    except requests.exceptions.ConnectionError:
        self.url = None
        log.warning('Unable to connect using urls: %s' % set([self.ext_url,
            self.local_url]))
        return False