def ffmpeg_works():
    images = np.zeros((2, 32, 32, 3), dtype=np.uint8)
    try:
        _encode_gif(images, 2)
        return True
    except (IOError, OSError):
        return False