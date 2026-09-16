async def flush(self, request: Request, stacks: List[Stack]):
    ns: List[Stack] = []
    for stack in stacks:
        ns.extend(self.typify(stack))
    if len(ns) > 1 and ns[-1] == Stack([lyr.Typing()]):
        ns[-1].get_layer(lyr.Typing).active = False
    await self.next(request, ns)