def favorites_getPublicList(user_id, per_page='', page=''):
    method = 'flickr.favorites.getPublicList'
    data = _doget(method, auth=False, user_id=user_id, per_page=per_page,
        page=page)
    photos = []
    if isinstance(data.rsp.photos.photo, list):
        for photo in data.rsp.photos.photo:
            photos.append(_parse_photo(photo))
    else:
        photos = [_parse_photo(data.rsp.photos.photo)]
    return photos