def _find_matching_algo(self, region):
    for algo in self._info.algos:
        algoStart = int(algo.attrib['start'], base=0)
        algoSize = int(algo.attrib['size'], base=0)
        algoEnd = algoStart + algoSize - 1
        if (algoStart <= region.start <= algoEnd and algoStart <= region.
            end <= algoEnd):
            return algo
    return None