def get_trees(self, data, showerrors=False):
    if not all(check(self._productionset.alphabet, [x]) for x in data):
        raise ValueError('Unknown element in {}, alphabet:{}'.format(str(
            data), self.productionset.alphabet))
    result = self.__recursive_parser(self._productionset.initialsymbol,
        data, self._productionset.main_production, showerrors)
    finalresult = []
    for eresult in result:
        if eresult.left == 0 and eresult.right == len(data
            ) and eresult not in finalresult:
            finalresult.append(eresult)
    return finalresult