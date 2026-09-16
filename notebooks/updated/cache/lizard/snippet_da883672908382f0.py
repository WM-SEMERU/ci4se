def __traces_url(self):
    path = AGENT_TRACES_PATH % self.from_.pid
    return 'http://%s:%s/%s' % (self.host, self.port, path)