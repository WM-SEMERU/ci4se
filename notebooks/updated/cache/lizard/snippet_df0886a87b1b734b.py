def autodiscover():
    global _RACE_PROTECTION
    if _RACE_PROTECTION:
        return
    _RACE_PROTECTION = True
    try:
        return filter(None, [find_related_module(app, 'tasks') for app in
            settings.INSTALLED_APPS])
    finally:
        _RACE_PROTECTION = False