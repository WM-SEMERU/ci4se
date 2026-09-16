def existing_social_friends(self, user_social_auth=None, friend_ids=None):
    self.assert_user_is_social_auth_user(user_social_auth)
    if not friend_ids:
        friend_ids = self.fetch_social_friend_ids(user_social_auth)
    if isinstance(friend_ids, basestring):
        friend_ids = eval(friend_ids)
    if USING_ALLAUTH:
        return User.objects.filter(socialaccount__uid__in=friend_ids).all()
    else:
        return User.objects.filter(social_auth__uid__in=friend_ids).all()