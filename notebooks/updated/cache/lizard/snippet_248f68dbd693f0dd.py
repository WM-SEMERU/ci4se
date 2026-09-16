def has_apps(names, check_platform=True):
    if check_platform:
        Environment._platform_is_windows()
    for name in names:
        yield Environment.has_app(str(name), check_platform=False)