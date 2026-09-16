def press(self):

    @param_to_property(key=['home', 'back', 'left', 'right', 'up', 'down',
        'center', 'menu', 'search', 'enter', 'delete', 'del', 'recent',
        'volume_up', 'volume_down', 'volume_mute', 'camera', 'power'])
    def _press(key, meta=None):
        if isinstance(key, int):
            return self.server.jsonrpc.pressKeyCode(key, meta
                ) if meta else self.server.jsonrpc.pressKeyCode(key)
        else:
            return self.server.jsonrpc.pressKey(str(key))
    return _press