def get_user(self, username, *, mode=OsuMode.osu, event_days=31):
    return self._make_req(endpoints.USER, dict(k=self.key, u=username, type
        =_username_type(username), m=mode.value, event_days=event_days),
        JsonList(User))