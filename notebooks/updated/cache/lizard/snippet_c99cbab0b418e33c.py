def list_images(profile, location_id=None, **libcloud_kwargs):
    conn = _get_driver(profile=profile)
    libcloud_kwargs = salt.utils.args.clean_kwargs(**libcloud_kwargs)
    if location_id is not None:
        location = _get_by_id(conn.list_locations(), location_id)
    else:
        location = None
    images = conn.list_images(location=location, **libcloud_kwargs)
    ret = []
    for image in images:
        ret.append(_simple_image(image))
    return ret