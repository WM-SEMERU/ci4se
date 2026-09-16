def random_color_func(word=None, font_size=None, position=None, orientation
    =None, font_path=None, random_state=None):
    if random_state is None:
        random_state = Random()
    return 'hsl(%d, 80%%, 50%%)' % random_state.randint(0, 255)