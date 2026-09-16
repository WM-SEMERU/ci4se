def automatic_slug_renaming(slug, is_slug_safe):
    if not isinstance(is_slug_safe, collections.Callable):
        raise TypeError('is_slug_safe must be callable')
    if is_slug_safe(slug):
        return slug
    count = 2
    new_slug = slug + '-' + str(count)
    while not is_slug_safe(new_slug):
        count = count + 1
        new_slug = slug + '-' + str(count)
    return new_slug