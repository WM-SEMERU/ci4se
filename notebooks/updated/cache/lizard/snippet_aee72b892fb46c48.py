def GetForwardedIps(self, interface, interface_ip=None):
    args = ['ls', 'table', 'local', 'type', 'local']
    options = self._CreateRouteOptions(dev=interface)
    result = self._RunIpRoute(args=args, options=options)
    result = re.sub('local\\s', '', result)
    return self.ParseForwardedIps(result.split())