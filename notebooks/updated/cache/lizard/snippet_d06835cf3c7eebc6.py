def static_full_sizes(width, height, tilesize):
    for level in range(0, 20):
        factor = 2.0 ** level
        sw = int(width / factor + 0.5)
        sh = int(height / factor + 0.5)
        if sw < tilesize and sh < tilesize:
            if sw < 1 or sh < 1:
                break
            yield [sw, sh]