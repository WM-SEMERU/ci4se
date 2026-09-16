def blpop(self, keys, timeout=0):
    map = {self.redis_key(k): k for k in self._parse_values(keys)}
    keys = map.keys()
    with self.pipe as pipe:
        f = Future()
        res = pipe.blpop(keys, timeout=timeout)

        def cb():
            if res.result:
                k = map[res.result[0]]
                v = self.valueparse.decode(res.result[1])
                f.set((k, v))
            else:
                f.set(res.result)
        pipe.on_execute(cb)
        return f