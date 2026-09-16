def abbreviate_list(items, max_items=10, item_max_len=40, joiner=', ',
    indicator='...'):
    if not items:
        return items
    else:
        shortened = [abbreviate_str('%s' % item, max_len=item_max_len) for
            item in items[0:max_items]]
        if len(items) > max_items:
            shortened.append(indicator)
        return joiner.join(shortened)