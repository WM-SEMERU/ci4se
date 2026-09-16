def add_item(c, name, item):
    if isinstance(item, MenuItem):
        if name not in c.items:
            c.items[name] = []
        c.items[name].append(item)
        c.sorted[name] = False