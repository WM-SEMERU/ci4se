def get_email(sciper):
    attribute = 'mail'
    response = LDAP_search(pattern_search='(uniqueIdentifier={})'.format(
        sciper), attribute=attribute)
    try:
        email = get_attribute(response, attribute)
    except Exception:
        raise EpflLdapException('No email address corresponds to sciper {}'
            .format(sciper))
    return email