def ips(self):
    r = []
    names = ['X_FORWARDED_FOR', 'CLIENT_IP', 'X_REAL_IP', 'X_FORWARDED',
        'X_CLUSTER_CLIENT_IP', 'FORWARDED_FOR', 'FORWARDED', 'VIA',
        'REMOTE_ADDR']
    for name in names:
        vs = self.get_header(name, '')
        if vs:
            r.extend(map(lambda v: v.strip(), vs.split(',')))
        vs = self.environ.get(name, '')
        if vs:
            r.extend(map(lambda v: v.strip(), vs.split(',')))
    return r