def toggle(user, obj):
    if Follow.objects.is_following(user, obj):
        return unfollow(user, obj)
    return follow(user, obj)