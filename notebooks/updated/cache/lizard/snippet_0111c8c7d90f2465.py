def decision(self, result, **values):
    data = self.__getDecision(result, **values)
    data = [data[value] for value in result]
    if len(data) == 1:
        return data[0]
    else:
        return data