async def iter_lines(self, chunk_size=1024):
    pending = b''
    async for chunk in self.iter_chunks(chunk_size):
        lines = (pending + chunk).splitlines(True)
        for line in lines[:-1]:
            await yield_(line.splitlines()[0])
        pending = lines[-1]
    if pending:
        await yield_(pending.splitlines()[0])