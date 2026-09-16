async def FirewallRules(self, known_services):
    _params = dict()
    msg = dict(type='Firewaller', request='FirewallRules', version=5,
        params=_params)
    _params['known-services'] = known_services
    reply = await self.rpc(msg)
    return reply