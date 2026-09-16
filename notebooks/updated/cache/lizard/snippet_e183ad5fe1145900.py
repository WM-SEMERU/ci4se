def get_group_category(self, category):
    category_id = obj_or_id(category, 'category', (GroupCategory,))
    response = self.__requester.request('GET', 'group_categories/{}'.format
        (category_id))
    return GroupCategory(self.__requester, response.json())