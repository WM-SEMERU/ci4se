def check_connection(self):
    host = self.urlparts[1]
    addresses = socket.getaddrinfo(host, 80, 0, 0, socket.SOL_TCP)
    args = {'host': host}
    if addresses:
        args['ips'] = [x[4][0] for x in addresses]
        self.set_result(_('%(host)s resolved to IPs %(ips)s') % args, valid
            =True)
    else:
        self.set_result(_('%(host)r could not be resolved') % args, valid=False
            )