def matchSubset(**kwargs):
    ret = []
    for m in self.matches:
        allMatched = True
        for k, v in iteritems(kwargs):
            mVal = getattr(m, k)
            try:
                if v == mVal or v in mVal:
                    continue
            except Exception:
                pass
            allMatched = False
            break
        if allMatched:
            ret.append(m)
    return ret