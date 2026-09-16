def decode(slug):
    if sys.version_info.major != 2 and isinstance(slug, bytes):
        slug = slug.decode('ascii')
    slug = slug + '=='
    return uuid.UUID(bytes=base64.urlsafe_b64decode(slug))