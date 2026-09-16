def get(cls, content_type_id):
    for content_type in cls.__CACHE__:
        if content_type.sys.get('id') == content_type_id:
            return content_type
    return None