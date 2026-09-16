async def rotate(self, source: str, dest: str):
    if self.rotator is None:
        if await self.loop.run_in_executor(None, lambda : os.path.exists(
            source)):
            await self.loop.run_in_executor(None, lambda : os.rename(source,
                dest))
    else:
        self.rotator(source, dest)