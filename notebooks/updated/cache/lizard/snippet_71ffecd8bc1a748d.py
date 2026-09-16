def clean(self, elements):
    cleanelements = []
    for i in xrange(len(elements)):
        if isempty(elements[i]):
            return []
        next = elements[i]
        if isinstance(elements[i], (list, tuple)):
            next = self.clean(elements[i])
        if next:
            cleanelements.append(elements[i])
    return cleanelements