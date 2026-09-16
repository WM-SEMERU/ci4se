async def service_status(self, name):
    return await self.send_command(OPERATIONS.CMD_QUERY_STATUS, {'name':
        name}, MESSAGES.QueryStatusResponse, timeout=5.0)