def get_entry_tags(self, categories):
    tags = []
    for category in categories:
        domain = category.attrib.get('domain', 'category')
        if 'tag' in domain and category.attrib.get('nicename'):
            tags.append(category.attrib.get('nicename'))
    return tags