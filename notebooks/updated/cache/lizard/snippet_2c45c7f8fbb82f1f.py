def display_image_file(fn, width='auto', height='auto',
    preserve_aspect_ratio=None):
    with open(os.path.realpath(os.path.expanduser(fn)), 'rb') as f:
        sys.stdout.buffer.write(image_bytes(f.read(), filename=fn, width=
            width, height=height, preserve_aspect_ratio=preserve_aspect_ratio))