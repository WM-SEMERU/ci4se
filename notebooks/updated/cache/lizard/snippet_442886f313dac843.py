def _get_hosts(self, patterns):
    hosts = set()
    for p in patterns:
        if p.startswith('!'):
            hosts.difference_update(self.__get_hosts(p))
        elif p.startswith('&'):
            hosts.intersection_update(self.__get_hosts(p))
        else:
            hosts.update(self.__get_hosts(p))
    return hosts