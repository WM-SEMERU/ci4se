def list_items(self, package_keyname, **kwargs):
    get_kwargs = {}
    get_kwargs['mask'] = kwargs.get('mask', ITEM_MASK)
    if 'filter' in kwargs:
        get_kwargs['filter'] = kwargs['filter']
    package = self.get_package_by_key(package_keyname, mask='id')
    items = self.package_svc.getItems(id=package['id'], **get_kwargs)
    return items