def has_app(name, check_platform=True):
    if check_platform:
        Environment._platform_is_windows()
    return which(str(name)) is not None