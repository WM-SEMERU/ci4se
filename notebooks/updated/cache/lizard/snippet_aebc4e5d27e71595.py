def _checkMode(self, ax_args):
    mode = ax_args.get('mode')
    if isinstance(mode, bytes):
        mode = str(mode, encoding='utf-8')
    if mode != self.mode:
        if not mode:
            raise NotAXMessage()
        else:
            raise AXError('Expected mode %r; got %r' % (self.mode, mode))