def selected_cats(self, items):
    cats = []
    for item in items:
        if 'category' in item and item['category'] not in cats:
            cats.append(item['category'])
    return cats