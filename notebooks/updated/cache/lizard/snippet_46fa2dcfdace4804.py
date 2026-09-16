def item_extra_kwargs(self, action):
    item = self.format(action)
    item.pop('title', None)
    item['uri'] = item.pop('url')
    item['activity:verb'] = item.pop('verb')
    return item