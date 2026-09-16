def flattencopy(lst):
    thelist = copy.deepcopy(lst)
    list_is_nested = True
    while list_is_nested:
        keepchecking = False
        atemp = []
        for element in thelist:
            if isinstance(element, list):
                atemp.extend(element)
                keepchecking = True
            else:
                atemp.append(element)
        list_is_nested = keepchecking
        thelist = atemp[:]
    return thelist