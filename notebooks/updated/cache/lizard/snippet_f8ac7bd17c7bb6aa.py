def _find_colour(particle, start_index, screen_data):
    _, fg2, attr2, bg2 = screen_data
    index = start_index
    for i, colours in enumerate(particle.colours):
        if (fg2, attr2, bg2) == colours:
            index = i
            break
    return index