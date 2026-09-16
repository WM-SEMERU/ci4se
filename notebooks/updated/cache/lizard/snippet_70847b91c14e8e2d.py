def get_colour(index):
    colours = ['red', 'blue', 'green', 'pink', 'yellow', 'magenta',
        'orange', 'cyan']
    default_colour = 'purple'
    if index < len(colours):
        return colours[index]
    else:
        return default_colour