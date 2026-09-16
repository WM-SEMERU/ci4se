async def ack(self, tube, task_id):
    cmd = tube.cmd('ack')
    args = task_id,
    res = await self.tnt.call(cmd, args)
    return res