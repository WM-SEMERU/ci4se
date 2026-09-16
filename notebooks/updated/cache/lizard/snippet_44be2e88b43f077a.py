def cmd_server_load(self):
    servers = defaultdict(int)
    for line in self._valid_lines:
        servers[line.server_name] += 1
    return servers