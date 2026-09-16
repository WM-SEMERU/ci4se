def get(self, request, bot_id, hook_id, id, format=None):
    bot = self.get_bot(bot_id, request.user)
    hook = self.get_hook(hook_id, bot, request.user)
    recipient = self.get_recipient(id, hook, request.user)
    serializer = self.serializer(recipient)
    return Response(serializer.data)