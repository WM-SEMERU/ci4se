def display_image_bytes(b, filename=None, inline=1, width='auto', height=
    'auto', preserve_aspect_ratio=None):
    sys.stdout.buffer.write(image_bytes(b, filename=filename, inline=inline,
        width=width, height=height, preserve_aspect_ratio=
        preserve_aspect_ratio))
    sys.stdout.write('\n')