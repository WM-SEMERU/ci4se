def get_user_info(apikey, username, password):
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return user_structure(user, site)