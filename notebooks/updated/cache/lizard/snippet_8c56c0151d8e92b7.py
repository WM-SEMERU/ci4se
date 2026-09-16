def fromInputs(self, inputs):
    outputs = []
    for i in xrange(self.count):
        name = self.name + '_' + str(i)
        try:
            value = inputs[name][0]
        except KeyError:
            raise ConfigurationError('Missing value for field %d of %s' % (
                i, self.name))
        else:
            outputs.append(maybeDeferred(self.coercer, value))
    return gatherResults(outputs)