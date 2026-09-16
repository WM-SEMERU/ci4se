def describe(self):
    result = 'No description available'
    if self.description:
        result = '%s' % self.description
    elif self.__doc__:
        s = []
        s += [self.__doc__.strip().replace('\n', '').replace('    ', ' ')]
        result = '\n'.join(s)
    return result