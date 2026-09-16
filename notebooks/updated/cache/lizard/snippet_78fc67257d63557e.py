def register(self, module, *args, **kwargs):
    from i3pystatus.text import Text
    if not module:
        return
    hints = self.default_hints.copy() if self.default_hints else {}
    hints.update(kwargs.get('hints', {}))
    if hints:
        kwargs['hints'] = hints
    try:
        return self.modules.append(module, *args, **kwargs)
    except Exception as e:
        log.exception(e)
        return self.modules.append(Text(color='#FF0000', text=
            '{i3py_mod}: Fatal Error - {ex}({msg})'.format(i3py_mod=module,
            ex=e.__class__.__name__, msg=e)))