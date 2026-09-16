def _default(self):
    if self.ctx.ignore_default:
        if not self.ctx.ignore_missing:
            self.ctx.errors.missing()
        return NOT_SET
    if self.default is NOT_SET:
        if not self.ctx.ignore_missing:
            self.ctx.errors.missing()
        return NOT_SET
    if self.default in IGNORE:
        return self.default
    if isinstance(self.default, Hook):
        if self.default:
            return self.default()
        if not self.ctx.ignore_missing:
            self.ctx.errors.missing()
        return NOT_SET
    if isinstance(self.default, type) or callable(self.default):
        return self.default()
    return self.default