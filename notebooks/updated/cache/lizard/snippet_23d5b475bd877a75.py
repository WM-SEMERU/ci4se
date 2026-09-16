def to_rgba(colors, dtype=np.uint8):
    if not util.is_sequence(colors):
        return
    colors = np.asanyarray(colors)
    opaque = np.iinfo(dtype).max
    if colors.dtype.kind == 'f' and colors.max() < 1.0 + 1e-08:
        colors = (colors * opaque).astype(dtype)
    elif colors.max() <= opaque:
        colors = colors.astype(dtype)
    else:
        raise ValueError('colors non- convertible!')
    if util.is_shape(colors, (-1, 3)):
        colors = np.column_stack((colors, opaque * np.ones(len(colors)))
            ).astype(dtype)
    elif util.is_shape(colors, (3,)):
        colors = np.append(colors, opaque)
    if not (util.is_shape(colors, (4,)) or util.is_shape(colors, (-1, 4))):
        raise ValueError('Colors not of appropriate shape!')
    return colors