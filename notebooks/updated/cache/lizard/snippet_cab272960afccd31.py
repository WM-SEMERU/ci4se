def check(cls, video):
    if not isinstance(video, cls.video_types):
        return False
    if cls.required_hash is not None and cls.required_hash not in video.hashes:
        return False
    return True