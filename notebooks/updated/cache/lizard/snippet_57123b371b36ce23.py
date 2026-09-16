async def forget_ticket(self, request):
    session = await get_session(request)
    session.pop(self.cookie_name, '')