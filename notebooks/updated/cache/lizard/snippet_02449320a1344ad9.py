def rule(self):
    if self._rule:
        return self._rule
    return self._make_rule(member_param=self._member_param,
        unique_member_param=self._unique_member_param)