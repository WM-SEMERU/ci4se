def _check_role(self):
    role = 'any'
    if 'role' in self.lti_kwargs:
        role = self.lti_kwargs['role']
    log.debug('check_role lti_role=%s decorator_role=%s', self.role, role)
    if not (role == 'any' or self.is_role(self, role)):
        raise LTIRoleException('Not authorized.')