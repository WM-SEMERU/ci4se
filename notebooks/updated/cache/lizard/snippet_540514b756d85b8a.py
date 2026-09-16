def as_dict(self):
    drepr = {'blocks': [block.as_dict() for block in self if block.hidden ==
        False], 'args': list(self.needed_inputs())}
    return drepr