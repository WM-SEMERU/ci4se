def as_list_with_options(self):
    it = ROOT.TIter(self)
    elem = it.Next()
    result = []
    while elem:
        if it.GetOption():
            result.append(TListItemWithOption(elem, it.GetOption()))
        else:
            result.append(elem)
        elem = it.Next()
    return result