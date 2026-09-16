async def pre_handle(self, request: Request, responder: 'Responder'):
    responder.send([lyr.Typing()])
    await responder.flush(request)
    responder.clear()
    await self.next(request, responder)