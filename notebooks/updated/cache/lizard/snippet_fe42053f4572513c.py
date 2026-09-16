def get_policy(self):
    if not self._policy:
        self._policy = self.policy_class(self._maps, self._clients)
    return self._policy