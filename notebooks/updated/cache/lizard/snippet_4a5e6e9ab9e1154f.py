def from_csv(cls, filename: str):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=unicode2str(','), quotechar=
            unicode2str('"'), quoting=csv.QUOTE_MINIMAL)
        entries = list()
        header_read = False
        elements = None
        for row in reader:
            if not header_read:
                elements = row[1:len(row) - 1]
                header_read = True
            else:
                name = row[0]
                energy = float(row[-1])
                comp = dict()
                for ind in range(1, len(row) - 1):
                    if float(row[ind]) > 0:
                        comp[Element(elements[ind - 1])] = float(row[ind])
                entries.append(PDEntry(Composition(comp), energy, name))
    return cls(entries)