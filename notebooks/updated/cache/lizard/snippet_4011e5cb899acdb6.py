async def unsubscribe(self, topic: str):
    req_msg = {'type': 'unsubscribe', 'topic': topic, 'response': True}
    await self._conn.send_message(req_msg)