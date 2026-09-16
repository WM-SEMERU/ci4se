def get_display_name(self, room=None):
    if room:
        try:
            return room.members_displaynames[self.user_id]
        except KeyError:
            return self.user_id
    if not self.displayname:
        self.displayname = self.api.get_display_name(self.user_id)
    return self.displayname or self.user_id