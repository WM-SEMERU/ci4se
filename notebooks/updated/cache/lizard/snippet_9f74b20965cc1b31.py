def logstats(self):
    lines = ['node {} current stats'.format(self),
        '--------------------------------------------------------',
        'node inbox size         : {}'.format(len(self.nodeInBox)),
        'client inbox size       : {}'.format(len(self.clientInBox)),
        'age (seconds)           : {}'.format(time.time() - self.created),
        'next check for reconnect: {}'.format(time.perf_counter() - self.
        nodestack.nextCheck), 'node connections        : {}'.format(self.
        nodestack.conns), 'f                       : {}'.format(self.f),
        'master instance         : {}'.format(self.instances.masterId),
        'replicas                : {}'.format(len(self.replicas)),
        'view no                 : {}'.format(self.viewNo),
        'rank                    : {}'.format(self.rank),
        'msgs to replicas        : {}'.format(self.replicas.sum_inbox_len),
        'msgs to view changer    : {}'.format(len(self.msgsToViewChanger)),
        'action queue            : {} {}'.format(len(self.actionQueue), id(
        self.actionQueue)), 'action queue stash      : {} {}'.format(len(
        self.aqStash), id(self.aqStash))]
    logger.info('\n'.join(lines), extra={'cli': False})