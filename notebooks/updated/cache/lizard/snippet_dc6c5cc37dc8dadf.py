def is_conditional(self, include_loop=True):
    if self.contains_if(include_loop) or self.contains_require_or_assert():
        return True
    if self.irs:
        last_ir = self.irs[-1]
        if last_ir:
            if isinstance(last_ir, Return):
                for r in last_ir.read:
                    if r.type == ElementaryType('bool'):
                        return True
    return False