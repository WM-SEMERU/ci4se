def get_lowest_decomposition(self, composition):
    entries_list = []
    elements = [e.symbol for e in composition.elements]
    for i in range(len(elements)):
        for combi in itertools.combinations(elements, i + 1):
            chemsys = [Element(e) for e in combi]
            x = self.costdb.get_entries(chemsys)
            entries_list.extend(x)
    try:
        pd = PhaseDiagram(entries_list)
        return pd.get_decomposition(composition)
    except IndexError:
        raise ValueError(
            'Error during PD building; most likely, cost data does not exist!')