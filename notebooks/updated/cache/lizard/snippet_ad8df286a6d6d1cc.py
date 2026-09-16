def prepend_items(self, items, **kwargs):
    rv = self.prepend_multi(items, **kwargs)
    for k, v in items.dict.items():
        if k.success:
            k.value = v['fragment'] + k.value
    return rv