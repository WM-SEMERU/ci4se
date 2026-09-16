def fetchImageUrl(self, image_id):
    image_id = str(image_id)
    data = {'photo_id': str(image_id)}
    j = self._get(ReqUrl.ATTACHMENT_PHOTO, query=data, fix_request=True,
        as_json=True)
    url = get_jsmods_require(j, 3)
    if url is None:
        raise FBchatException('Could not fetch image url from: {}'.format(j))
    return url