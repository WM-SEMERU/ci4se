def item_hist(list_):
    dict_hist = {}
    for item in list_:
        if item not in dict_hist:
            dict_hist[item] = 0
        dict_hist[item] += 1
    return dict_hist