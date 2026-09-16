def is_resource_protected(self, request, **kwargs):
    access_state = self._get_resource_access_state(request)
    protected_states = self.get_protected_states()
    return access_state in protected_states