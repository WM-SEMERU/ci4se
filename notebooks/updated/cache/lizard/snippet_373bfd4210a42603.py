def getStreamNetworkAsWkt(self, session, withNodes=True):
    wkt_list = []
    for link in self.streamLinks:
        wkt_link = link.getAsWkt(session)
        if wkt_link:
            wkt_list.append(wkt_link)
        if withNodes:
            for node in link.nodes:
                wkt_node = node.getAsWkt(session)
                if wkt_node:
                    wkt_list.append(wkt_node)
    return 'GEOMCOLLECTION ({0})'.format(', '.join(wkt_list))