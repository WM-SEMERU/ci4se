def addCodedValue(self, name, code):
    i = {'name': name, 'code': code}
    if i not in self._codedValues:
        self._codedValues.append(i)