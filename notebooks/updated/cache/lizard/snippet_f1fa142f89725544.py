def png(out, metadata, f):
    import png
    pixels, meta = pixmeta(metadata, f)
    p = png.Writer(**meta)
    p.write(out, pixels)