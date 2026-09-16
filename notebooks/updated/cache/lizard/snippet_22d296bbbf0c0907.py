async def immediate_execute_command(self, *args, **options):
    command_name = args[0]
    conn = self.connection
    if not conn:
        conn = self.connection_pool.get_connection()
        self.connection = conn
    try:
        await conn.send_command(*args)
        return await self.parse_response(conn, command_name, **options)
    except (ConnectionError, TimeoutError) as e:
        conn.disconnect()
        if not conn.retry_on_timeout and isinstance(e, TimeoutError):
            raise
        try:
            if not self.watching:
                await conn.send_command(*args)
                return await self.parse_response(conn, command_name, **options)
        except ConnectionError:
            conn.disconnect()
            await self.reset()
            raise