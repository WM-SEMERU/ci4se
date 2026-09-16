def get_contributor_sort_value(self, obj):
    user = obj.contributor
    if user.first_name or user.last_name:
        contributor = user.get_full_name()
    else:
        contributor = user.username
    return contributor.strip().lower()