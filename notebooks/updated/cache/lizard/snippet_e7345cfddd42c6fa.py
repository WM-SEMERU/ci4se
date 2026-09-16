async def debug(self, conn_id, name, cmd_args):
    adapter_id = self._get_property(conn_id, 'adapter')
    return await self.adapters[adapter_id].debug(conn_id, name, cmd_args)