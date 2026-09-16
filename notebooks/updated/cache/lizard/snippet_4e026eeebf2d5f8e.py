def pfcount(self, *sources):
    sources = [self.redis_key(s) for s in sources]
    with self.pipe as pipe:
        return pipe.execute_command('PFCOUNT', *sources)