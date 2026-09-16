def get_unread_forums_from_list(self, user, forums):
    unread_forums = []
    if not user.is_authenticated:
        return unread_forums
    unread = ForumReadTrack.objects.get_unread_forums_from_list(forums, user)
    unread_forums.extend(unread)
    return unread_forums