def get_redis_client(self):
    host = self.config['host']
    ports = self.config['ports']
    sentinel_ports = self.config['sentinel_ports']
    sentinel_name = self.config['sentinel_name']
    password = self.config['password']
    databases = self.config['databases']
    if not isinstance(ports, list):
        ports = [ports]
    if not isinstance(sentinel_ports, list):
        sentinel_ports = [sentinel_ports]
    if sentinel_ports:
        assert len(sentinel_ports) == len(ports)
    else:
        sentinel_ports = [None for _ in xrange(len(ports))]
    for port, sentinel_port in izip(ports, sentinel_ports):
        for db in xrange(0, int(databases)):
            master = self.get_master(host, port, sentinel_port, sentinel_name)
            pool = redis.ConnectionPool(host=master[0], port=int(master[1]),
                password=password, db=db)
            yield redis.Redis(connection_pool=pool), port, db