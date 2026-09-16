def get(self, request, provider=None):
    if USING_ALLAUTH:
        self.social_auths = request.user.socialaccount_set.all()
    else:
        self.social_auths = request.user.social_auth.all()
    self.social_friend_lists = []
    if self.social_auths.count() == 0:
        if REDIRECT_IF_NO_ACCOUNT:
            return HttpResponseRedirect(REDIRECT_URL)
        return super(FriendListView, self).get(request)
    self.social_friend_lists = (SocialFriendList.objects.
        get_or_create_with_social_auths(self.social_auths))
    return super(FriendListView, self).get(request)