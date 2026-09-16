async def get_group_memory(self):
    act = self.service.action('X_GetAllGroupMemory')
    res = await act.async_call()
    return res