def get_nets_lacnic(self, response):
    nets = []
    for match in re.finditer(
        '^(inetnum|inet6num|route):[^\\S\\n]+(.+?,[^\\S\\n].+|.+)$',
        response, re.MULTILINE):
        try:
            net = copy.deepcopy(BASE_NET)
            net_range = match.group(2).strip()
            try:
                net['range'] = net['range'] = '{0} - {1}'.format(ip_network
                    (net_range)[0].__str__(), ip_network(net_range)[-1].
                    __str__()) if '/' in net_range else net_range
            except ValueError:
                net['range'] = net_range
            temp = []
            for addr in net_range.split(', '):
                count = addr.count('.')
                if count is not 0 and count < 4:
                    addr_split = addr.strip().split('/')
                    for i in range(count + 1, 4):
                        addr_split[0] += '.0'
                    addr = '/'.join(addr_split)
                temp.append(ip_network(addr.strip()).__str__())
            net['cidr'] = ', '.join(temp)
            net['start'] = match.start()
            net['end'] = match.end()
            nets.append(net)
        except ValueError:
            pass
    return nets