async def debug_command_message(self, message, context):
    conn_string = message.get('connection_string')
    command = message.get('command')
    args = message.get('args')
    client_id = context.user_data
    result = await self.debug(client_id, conn_string, command, args)
    return result