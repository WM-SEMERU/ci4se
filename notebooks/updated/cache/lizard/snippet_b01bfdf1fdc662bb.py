def forum_list_filter(self, qs, user):
    if user.is_superuser:
        return qs
    forums_to_hide = self._get_hidden_forum_ids(qs, user)
    return qs.exclude(id__in=forums_to_hide)