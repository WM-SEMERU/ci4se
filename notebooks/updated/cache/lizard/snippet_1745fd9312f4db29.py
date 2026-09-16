def _assert_category(self, category):
    category = category.lower()
    valid_categories = ['cable', 'broadcast', 'final', 'tv']
    assert_msg = '%s is not a valid category.' % category
    assert category in valid_categories, assert_msg