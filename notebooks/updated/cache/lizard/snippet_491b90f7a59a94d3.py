async def SetExternalControllerInfo(self, controllers):
    _params = dict()
    msg = dict(type='ExternalControllerUpdater', request=
        'SetExternalControllerInfo', version=1, params=_params)
    _params['controllers'] = controllers
    reply = await self.rpc(msg)
    return reply