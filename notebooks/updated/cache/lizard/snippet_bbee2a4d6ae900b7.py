def _manageTags(tagList, guids, add=True):
    objects = getObjectsFromGuids(guids)
    tags = []
    for tag in tagList:
        try:
            t = Tag.objects.get(pk=int(tag))
        except ValueError:
            t = Tag.objects.get_or_create(name=tag.lower())[0]
        tags.append(t)
    if add:
        return _addTags(tags, objects)
    else:
        return _removeTags(tags, objects)