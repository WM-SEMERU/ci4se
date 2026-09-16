def has_friends(self, flt=FriendFilter.ALL):
    return self._iface.get_has_friend(self.user_id, flt)