def new(cls, package, media):
    partname = package.next_media_partname(media.ext)
    return cls(partname, media.content_type, media.blob, package)