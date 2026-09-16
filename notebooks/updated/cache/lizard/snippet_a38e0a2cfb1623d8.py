def controllers(self):
    controllers = []
    try:
        while True:
            controller = self.lib.tdController()
            del controller['name']
            del controller['available']
            controllers.append(Controller(lib=self.lib, **controller))
    except TelldusError as e:
        if e.error != const.TELLSTICK_ERROR_NOT_FOUND:
            raise
    return controllers