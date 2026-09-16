def object_to_items(data_structure):
    items = []
    try:
        items = list(data_structure.__dict__.items())
    except:
        pass
    hierarchy = [data_structure]
    try:
        hierarchy += inspect.getmro(data_structure)
    except:
        pass
    slots = []
    try:
        for b in hierarchy:
            try:
                slots += b.__slots__
            except:
                pass
    except:
        pass
    for x in slots:
        items.append((x, getattr(data_structure, x)))
    return items