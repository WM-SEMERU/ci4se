def var_expand(self, cmd, depth=0, formatter=DollarFormatter()):
    ns = self.user_ns.copy()
    try:
        frame = sys._getframe(depth + 1)
    except ValueError:
        pass
    else:
        ns.update(frame.f_locals)
    try:
        cmd = formatter.vformat(cmd, args=[], kwargs=ns)
    except Exception:
        pass
    return cmd