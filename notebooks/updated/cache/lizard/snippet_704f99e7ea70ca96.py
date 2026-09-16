def total_capacity(self):
    total_capacity = 0
    hosts = yield self.hosts(enabled=True)
    for host in hosts:
        total_capacity += host.capacity
    defer.returnValue(total_capacity)