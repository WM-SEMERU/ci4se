def depth(self):
    sub_categories = self._sub_categories
    if not sub_categories:
        return 1
    first_depth = sub_categories[0].depth
    for category in sub_categories[1:]:
        if category.depth != first_depth:
            raise ValueError('category depth not uniform')
    return first_depth + 1