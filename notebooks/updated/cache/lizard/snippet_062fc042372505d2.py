def get_current_usersettings():
    USERSETTINGS_MODEL = get_usersettings_model()
    try:
        current_usersettings = USERSETTINGS_MODEL.objects.get_current()
    except USERSETTINGS_MODEL.DoesNotExist:
        current_usersettings = USERSETTINGS_MODEL.get_default()
    return current_usersettings