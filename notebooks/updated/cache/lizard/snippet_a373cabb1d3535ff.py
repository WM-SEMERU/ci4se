def valid(self):
    valid_servers = 0
    for server in self._servers:
        if server['down_until'] <= time.time():
            valid_servers += 1
    return valid_servers > 0