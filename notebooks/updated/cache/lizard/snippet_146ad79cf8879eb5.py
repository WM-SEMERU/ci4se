def get_ldap_user_membership(self, user_dn):
    membership_filter = self.conf_LDAP_SYNC_GROUP_MEMBERSHIP_FILTER.replace(
        '{distinguishedName}', user_dn.replace('(', '\\(').replace(')', '\\)'))
    try:
        uri, groups = self.ldap_search(membership_filter, self.
            conf_LDAP_SYNC_GROUP_ATTRIBUTES.keys(), False, membership_filter)
    except Exception as e:
        logger.error('Error reading membership: Filter %s, Keys %s' % (
            membership_filter, str(self.conf_LDAP_SYNC_GROUP_ATTRIBUTES.
            keys())))
        return None
    return uri, groups