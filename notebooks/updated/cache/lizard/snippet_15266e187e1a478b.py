def chunk_count(swatch):
    if type(swatch) is dict:
        if 'data' in swatch:
            return 1
        if 'swatches' in swatch:
            return 2 + len(swatch['swatches'])
    else:
        return sum(map(chunk_count, swatch))