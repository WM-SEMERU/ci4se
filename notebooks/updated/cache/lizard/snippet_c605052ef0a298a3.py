def _stripe_object_to_subscription_items(cls, target_cls, data, subscription):
    items = data.get('items')
    if not items:
        return []
    subscriptionitems = []
    for item_data in items.get('data', []):
        item, _ = target_cls._get_or_create_from_stripe_object(item_data,
            refetch=False)
        subscriptionitems.append(item)
    return subscriptionitems