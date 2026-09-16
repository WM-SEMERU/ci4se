def create_items(sender, instance, **kwargs):
    if instance.item_id is None and instance.item is None:
        item = Item()
        if hasattr(instance, 'active'):
            item.active = getattr(instance, 'active')
        item.save()
        instance.item = item