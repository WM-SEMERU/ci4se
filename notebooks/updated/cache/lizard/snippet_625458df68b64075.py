def disconnect(self):
    old_api = object.__getattribute__(self, '_api')
    new_api = API.build_hardware_simulator(loop=old_api._loop, config=copy.
        copy(old_api.config))
    setattr(self, '_api', new_api)