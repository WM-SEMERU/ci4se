def delete_access_list_items(self, loadbalancer, item_ids):
    if not isinstance(item_ids, (list, tuple)):
        item_ids = [item_ids]
    valid_ids = [itm['id'] for itm in self.get_access_list(loadbalancer)]
    bad_ids = [str(itm) for itm in item_ids if itm not in valid_ids]
    if bad_ids:
        raise exc.AccessListIDNotFound(
            'The following ID(s) are not valid Access List items: %s' %
            ', '.join(bad_ids))
    items = '&'.join([('id=%s' % item_id) for item_id in item_ids])
    uri = '/loadbalancers/%s/accesslist?%s' % (utils.get_id(loadbalancer),
        items)
    resp, body = self.api.method_delete(uri)
    return body