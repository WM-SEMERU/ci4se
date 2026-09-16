def _server_whitelist(self):
    whitelist = []
    for server in self.servers:
        if server not in self.last_error or self.last_error[server
            ] < time.time() - self.PENALTY_BOX_TIME:
            whitelist.append(server)
    if not whitelist:
        whitelist.append(sorted(self.last_error.items(), key=lambda kv: kv[
            1])[0][0])
    return whitelist