def consume(self, msg):
    self.log.info(msg)
    body = msg['body']
    topic = body['topic']
    repo = None
    if 'rawhide' in topic:
        arch = body['msg']['arch']
        self.log.info('New rawhide %s compose ready', arch)
        repo = 'rawhide'
    elif 'branched' in topic:
        arch = body['msg']['arch']
        branch = body['msg']['branch']
        self.log.info('New %s %s branched compose ready', branch, arch)
        log = body['msg']['log']
        if log != 'done':
            self.log.warn('Compose not done?')
            return
        repo = branch
    elif 'updates.fedora' in topic:
        self.log.info('New Fedora %(release)s %(repo)s compose ready', body
            ['msg'])
        repo = 'f%(release)s-%(repo)s' % body['msg']
    else:
        self.log.warn('Unknown topic: %s', topic)
    release = self.releases[repo]
    reactor.callInThread(self.compose, release)