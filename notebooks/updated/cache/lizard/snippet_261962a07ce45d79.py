def gather(self, *futures: Union[asyncio.Future, asyncio.coroutine]):
    self.ft_count = len(futures)
    self.futures = asyncio.gather(*futures, loop=self.loop,
        return_exceptions=self.return_exceptions)