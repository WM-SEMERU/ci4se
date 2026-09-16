def get_steamids_from_ips(self, server_ips, timeout=30):
    resp, error = self._um.send_and_wait('GameServers.GetServerSteamIDsByIP#1',
        {'server_ips': server_ips}, timeout=timeout)
    if error:
        raise error
    if resp is None:
        return None
    return {server.addr: SteamID(server.steamid) for server in resp.servers}