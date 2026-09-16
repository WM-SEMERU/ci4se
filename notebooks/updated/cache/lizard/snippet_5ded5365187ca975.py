def get_absolute_url(self):
    from django.urls import NoReverseMatch
    if self.alternate_url:
        return self.alternate_url
    try:
        prefix = reverse('categories_tree_list')
    except NoReverseMatch:
        prefix = '/'
    ancestors = list(self.get_ancestors()) + [self]
    return prefix + '/'.join([force_text(i.slug) for i in ancestors]) + '/'