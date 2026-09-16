def getKendallTauScore(myResponse, otherResponse):
    kt = 0
    list1 = myResponse.values()
    list2 = otherResponse.values()
    if len(list1) <= 1:
        return kt
    for itr1 in range(0, len(list1) - 1):
        for itr2 in range(itr1 + 1, len(list2)):
            if list1[itr1] > list1[itr2] and list2[itr1] < list2[itr2
                ] or list1[itr1] < list1[itr2] and list2[itr1] > list2[itr2]:
                kt += 1
    kt = kt * 2 / (len(list1) * (len(list1) - 1))
    return kt