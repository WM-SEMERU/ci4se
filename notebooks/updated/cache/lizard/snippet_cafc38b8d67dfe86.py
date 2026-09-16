async def unban(self, user_id: base.Integer):
    return await self.bot.unban_chat_member(self.id, user_id=user_id)