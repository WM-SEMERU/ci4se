async def release(self, delay=None):
    the_tuple = await self.queue.release(self.tube, self.task_id, delay=delay)
    self.update_from_tuple(the_tuple)
    if delay is None:
        return bool(self.state == READY)
    else:
        return bool(self.state == DELAYED)