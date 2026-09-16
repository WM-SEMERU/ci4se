def clusterQueues(self):
    servers = yield self.getClusterServers()
    queues = {}
    for sname in servers:
        qs = yield self.get('rhumba.server.%s.queues' % sname)
        uuid = yield self.get('rhumba.server.%s.uuid' % sname)
        qs = json.loads(qs)
        for q in qs:
            if q not in queues:
                queues[q] = []
            queues[q].append({'host': sname, 'uuid': uuid})
    defer.returnValue(queues)