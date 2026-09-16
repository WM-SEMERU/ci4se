def findAllSingle(self, selfValue):
    resultList = []
    for element in selfValue:
        if isinstance(element, Single):
            resultList.append(element)
            resultList += element.findAllSingle()
    return resultList