async def got_who_reply(self, nick=None, real_name=None, **kws):
    nick = nick[2:] if nick[0:2] == 'E_' else nick
    host, ports = real_name.split(' ', 1)
    self.servers.remove(nick)
    logger.debug("Found: '%s' at %s with port list: %s", nick, host, ports)
    self.results[host.lower()] = ServerInfo(nick, host, ports)
    if not self.servers:
        self.all_done.set()