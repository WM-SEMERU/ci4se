def ssml_break(self, strength=None, time=None, **kwargs):
    return self.nest(SsmlBreak(strength=strength, time=time, **kwargs))