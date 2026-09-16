def _group_kids(self, node_one, node_two):
    in_1_not_in_2 = []
    in_2_not_in_1 = []
    in_1_and_in_2 = []
    for child in node_one.getchildren():
        peers = self._get_peers(child, node_two)
        if len(peers) < 1:
            in_1_not_in_2.append(child)
        elif len(peers) > 1:
            raise ConfigError('not unique peer of node {}'.format(self.
                device.get_xpath(child)))
        else:
            in_1_and_in_2.append((child, peers[0]))
    for child in node_two.getchildren():
        peers = self._get_peers(child, node_one)
        if len(peers) < 1:
            in_2_not_in_1.append(child)
        elif len(peers) > 1:
            raise ConfigError('not unique peer of node {}'.format(self.
                device.get_xpath(child)))
        else:
            pass
    return in_1_not_in_2, in_2_not_in_1, in_1_and_in_2