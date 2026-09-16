def fanout(self, hosts=None, timeout=None, max_concurrency=64, auto_batch=None
    ):
    return MapManager(self.get_fanout_client(hosts, max_concurrency,
        auto_batch), timeout=timeout)