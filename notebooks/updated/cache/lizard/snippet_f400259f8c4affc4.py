def ziptake(items_list, indexes_list):
    return [take(list_, index_list) for list_, index_list in zip(items_list,
        indexes_list)]