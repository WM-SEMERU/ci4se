def getConnectorStats(self):
    if self._statusxml is None:
        self.initStats()
    connnodes = self._statusxml.findall('connector')
    connstats = {}
    if connnodes:
        for connnode in connnodes:
            namestr = connnode.get('name')
            if namestr is not None:
                mobj = re.match('(.*)-(\\d+)', namestr)
                if mobj:
                    proto = mobj.group(1)
                    port = int(mobj.group(2))
                    connstats[port] = {'proto': proto}
                    for tag in ('threadInfo', 'requestInfo'):
                        stats = {}
                        node = connnode.find(tag)
                        if node is not None:
                            for key, val in node.items():
                                if re.search('Time$', key):
                                    stats[key] = float(val) / 1000.0
                                else:
                                    stats[key] = util.parse_value(val)
                        if stats:
                            connstats[port][tag] = stats
    return connstats