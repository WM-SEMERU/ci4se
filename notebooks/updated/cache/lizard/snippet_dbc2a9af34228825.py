def show_item(h):
    if isinstance(h, rf.Rar3Info):
        show_item_v3(h)
    elif isinstance(h, rf.Rar5Info):
        show_item_v5(h)
    else:
        xprint('Unknown info record')