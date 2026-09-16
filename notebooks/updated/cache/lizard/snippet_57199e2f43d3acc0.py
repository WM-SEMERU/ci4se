def matches(self, pattern):
    return ArrayPredicate(term=self, op=LabelArray.matches, opargs=(pattern,))