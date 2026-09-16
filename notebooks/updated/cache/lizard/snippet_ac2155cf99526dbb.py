def generate_unique_slug(field, instance, slug, manager):
    original_slug = slug = crop_slug(field, slug)
    default_lookups = tuple(get_uniqueness_lookups(field, instance, field.
        unique_with))
    index = 1
    if not manager:
        manager = field.model._default_manager
    while True:
        lookups = dict(default_lookups, **{field.name: slug})
        rivals = manager.filter(**lookups)
        if instance.pk:
            rivals = rivals.exclude(pk=instance.pk)
        if not rivals:
            return slug
        index += 1
        tail_length = len(field.index_sep) + len(str(index))
        combined_length = len(original_slug) + tail_length
        if field.max_length < combined_length:
            original_slug = original_slug[:field.max_length - tail_length]
        data = dict(slug=original_slug, sep=field.index_sep, index=index)
        slug = '%(slug)s%(sep)s%(index)d' % data