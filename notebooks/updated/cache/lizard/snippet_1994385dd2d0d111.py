def follow(user, obj):
    follow, created = Follow.objects.get_or_create(user, obj)
    return follow