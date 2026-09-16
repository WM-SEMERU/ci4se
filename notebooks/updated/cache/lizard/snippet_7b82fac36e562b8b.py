def settings(cls):
    from bernard.platforms.management import get_platform_settings
    for platform in get_platform_settings():
        candidate = import_class(platform['class'])
        if candidate == cls:
            return platform.get('settings', {})