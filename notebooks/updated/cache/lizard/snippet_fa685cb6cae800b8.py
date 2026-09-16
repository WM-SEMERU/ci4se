def users_with_birthday(self, month, day):
    users = User.objects.filter(properties___birthday__month=month,
        properties___birthday__day=day)
    results = []
    for user in users:
        results.append(user)
    return results