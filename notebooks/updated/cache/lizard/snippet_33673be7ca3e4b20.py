def safe_list_set(plist, idx, fill_with, value):
    try:
        plist[idx] = value
        return
    except IndexError:
        pass
    end = idx + 1 if idx >= 0 else abs(idx)
    for _ in range(len(plist), end):
        if callable(fill_with):
            plist.append(fill_with())
        else:
            plist.append(fill_with)
    plist[idx] = value