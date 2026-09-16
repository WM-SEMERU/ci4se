def forward(self, serial, remote, local_port=None):
    if isinstance(remote, int):
        remote = 'tcp:%d' % remote
    if not local_port:
        for s, lp, rp in self.forward_list():
            if s == serial and rp == remote:
                return int(lp[4:])
        return self.forward(serial, remote, next_local_port(self.server_host))
    else:
        self.raw_cmd('-s', serial, 'forward', 'tcp:%d' % local_port, remote
            ).wait()
        return local_port