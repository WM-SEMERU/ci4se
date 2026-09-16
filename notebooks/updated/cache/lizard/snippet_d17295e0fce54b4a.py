async def get_value(self):
    cc = self.request.custom_content
    async with self.lock:
        if self.content_key not in cc:
            cc[self.content_key] = await self.call_api()
    return cc[self.content_key]