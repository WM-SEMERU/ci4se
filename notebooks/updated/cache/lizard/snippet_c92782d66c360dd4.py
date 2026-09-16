def get_available_themes():
    for d in settings.TEMPLATE_DIRS:
        for _d in os.listdir(d):
            if os.path.isdir(os.path.join(d, _d)) and is_theme_dir(_d):
                yield _d