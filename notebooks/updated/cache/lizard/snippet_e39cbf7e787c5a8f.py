async def runCmdLine(self, line):
    opts = self.getCmdOpts(line)
    return await self.runCmdOpts(opts)