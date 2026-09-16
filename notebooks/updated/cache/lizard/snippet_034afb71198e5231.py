def who_has(self, subid):
    answer = []
    for name in self.__map:
        if subid in self.__map[name] and not name in answer:
            answer.append(name)
    return answer