def remove_member(self, user, api=None):
    api = api or self._API
    AutomationMember.remove(automation=self.id, user=user, api=api)