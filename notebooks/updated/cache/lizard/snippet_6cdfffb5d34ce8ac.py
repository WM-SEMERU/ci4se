def check_ips(self, addrs):
    tasks = []
    for addr in addrs:
        tasks.append(self._check_ip(addr))
    return self._loop.run_until_complete(asyncio.gather(*tasks))