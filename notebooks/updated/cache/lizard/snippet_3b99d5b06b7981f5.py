async def get_file(self):
    if hasattr(self, 'file_path'):
        return self
    else:
        return await self.bot.get_file(self.file_id)