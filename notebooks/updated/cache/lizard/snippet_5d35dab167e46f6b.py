def get_available_palettes(chosen_palette):
    result = None
    try:
        result = ALL_PALETTES[:ALL_PALETTES.index(chosen_palette) + 1]
    except ValueError:
        pass
    return result