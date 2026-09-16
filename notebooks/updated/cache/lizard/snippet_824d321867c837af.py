def frog_tip(self):
    cache = self._cache
    client = self._client
    if self.should_refresh:
        tips = client.croak()
        for number, tip in tips.items():
            cache[str(number)] = tip
    choice = random.choice(list(cache.keys()))
    try:
        tip = cache[choice].decode()
    except AttributeError:
        tip = cache[choice]
    del cache[choice]
    return tip