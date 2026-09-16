def get(typename):
    dt = getPDT(typename) or getCDT(typename)
    if dt is None:
        pdt, nelems = ArrayType.parse(typename)
        if pdt and nelems:
            dt = ArrayType(pdt, nelems)
    return dt