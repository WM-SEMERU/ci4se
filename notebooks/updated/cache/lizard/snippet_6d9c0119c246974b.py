def fetch_social_friend_ids(self, social_auth_user):
    self.assert_user_is_social_auth_user(social_auth_user)
    friends_provider = SocialFriendsFinderBackendFactory.get_backend(
        social_auth_user.provider)
    friend_ids = friends_provider.fetch_friend_ids(social_auth_user)
    return friend_ids