def image_search(auth=None, **kwargs):
    cloud = get_operator_cloud(auth)
    kwargs = _clean_kwargs(**kwargs)
    return cloud.search_images(**kwargs)