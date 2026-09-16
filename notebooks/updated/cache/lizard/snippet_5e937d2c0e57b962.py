async def update_chat(self):
    other = await self.bot.get_chat(self.id)
    for key, value in other:
        self[key] = value