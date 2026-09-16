def delete(request, obj_id=None):
    data = request.DELETE or json.loads(request.body)
    guids = data.get('guids').split(',')
    objects = getObjectsFromGuids(guids)
    gallery = Gallery.objects.get(pk=obj_id)
    LOGGER.info('{} removed {} from {}'.format(request.user.email, guids,
        gallery))
    for o in objects:
        if isinstance(o, Image):
            gallery.images.remove(o)
        elif isinstance(o, Video):
            gallery.videos.remove(o)
    res = Result()
    return JsonResponse(res.asDict())