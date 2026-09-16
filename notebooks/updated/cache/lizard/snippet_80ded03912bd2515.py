def clean_list(l0, clean_item_fn=None):
    clean_item_fn = clean_item_fn if clean_item_fn else clean_item
    l = list()
    for index, item in enumerate(l0):
        cleaned_item = clean_item_fn(item)
        l.append(cleaned_item)
    return l