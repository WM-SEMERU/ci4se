def get_users_indexed_by_lang():
    result = {}
    users = TransUser.objects.filter(active=True).select_related('user')
    for user in users:
        for lang in user.languages.all():
            if lang.code not in result:
                result[lang.code] = set()
            result[lang.code].add(user)
    return result