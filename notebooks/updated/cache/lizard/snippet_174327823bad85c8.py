async def set(self, key, value, param=None, expire_time=None, herd_timeout=None
    ):
    identity = self._gen_identity(key, param)
    expected_expired_ts = int(time.time())
    if expire_time:
        expected_expired_ts += expire_time
    expected_expired_ts += herd_timeout or self.default_herd_timeout
    value = self._pack([value, expected_expired_ts])
    return await self.client.set(identity, value, ex=expire_time)