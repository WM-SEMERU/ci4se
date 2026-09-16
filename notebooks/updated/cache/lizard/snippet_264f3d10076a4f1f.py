def clear_usersettings_cache(sender, **kwargs):
    instance = kwargs['instance']
    try:
        del USERSETTINGS_CACHE[instance.site.pk]
    except KeyError:
        pass