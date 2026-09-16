def is_role(self, role):
    log.debug('is_role %s', role)
    roles = self.session['roles'].split(',')
    if role in LTI_ROLES:
        role_list = LTI_ROLES[role]
        roles = set(role_list) & set(roles)
        is_user_role_there = len(roles) >= 1
        log.debug('is_role roles_list=%s role=%s in list=%s', role_list,
            roles, is_user_role_there)
        return is_user_role_there
    else:
        raise LTIException('Unknown role {}.'.format(role))