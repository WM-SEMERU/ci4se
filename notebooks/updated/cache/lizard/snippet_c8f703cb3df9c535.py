def connect(self, node, properties=None):
    if len(self):
        raise AttemptedCardinalityViolation(
            "Node already has {0} can't connect more".format(self))
    else:
        return super(ZeroOrOne, self).connect(node, properties)