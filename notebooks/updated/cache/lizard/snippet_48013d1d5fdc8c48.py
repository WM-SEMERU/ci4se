def log_with_color(level):

    def wrapper(text):
        color = log_colors_config[level.upper()]
        getattr(logger, level.lower())(coloring(text, color))
    return wrapper