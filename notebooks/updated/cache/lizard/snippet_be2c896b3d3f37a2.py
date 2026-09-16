def does_not_contain(self, element):
    self._run(unittest_case.assertNotIn, (element, self._subject))
    return ChainInspector(self._subject)