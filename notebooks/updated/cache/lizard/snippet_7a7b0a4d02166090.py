def write_switch(self, module_address, state, callback_fn):
    _LOGGER.info('write_switch: setstate,{},{}{}'.format(module_address,
        str(state), chr(13)))
    self.subscribe('state,' + module_address, callback_fn)
    self.send('setstate,{},{}{}'.format(module_address, str(state), chr(13)))