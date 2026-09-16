def HandleFilterMaxComponentLimit(handle, lfilter):
    from Ucs import AndFilter, OrFilter, AbstractFilter
    maxComponents = 10
    if lfilter == None or lfilter.GetChildCount() <= maxComponents:
        return lfilter
    if not isinstance(lfilter, AndFilter) and not isinstance(lfilter, OrFilter
        ):
        return lfilter
    resultFilter = None
    if isinstance(lfilter, AndFilter) == True:
        parentFilter = AndFilter()
        childFilter = AndFilter()
        parentFilter.AddChild(childFilter)
        for cf in lfilter.GetChild():
            if isinstance(cf, AbstractFilter) == True:
                if childFilter.GetChildCount() == maxComponents:
                    childFilter = AndFilter()
                    parentFilter.AddChild(childFilter)
                childFilter.AddChild(cf)
        resultFilter = parentFilter
    else:
        parentFilter = OrFilter()
        childFilter = OrFilter()
        parentFilter.AddChild(childFilter)
        for cf in lfilter.GetChild():
            if isinstance(cf, AbstractFilter) == True:
                if childFilter.GetChildCount() == maxComponents:
                    childFilter = OrFilter()
                    parentFilter.AddChild(childFilter)
                childFilter.AddChild(cf)
        resultFilter = parentFilter
    return UcsUtils.HandleFilterMaxComponentLimit(handle, resultFilter)