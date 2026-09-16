def _check_img_lib():
    imageio = PIL = None
    try:
        import imageio
    except ImportError:
        try:
            import PIL.Image
        except ImportError:
            pass
    return imageio, PIL