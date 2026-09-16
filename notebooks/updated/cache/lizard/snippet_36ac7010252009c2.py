def get_user_id(self, attributes):
    if not attributes:
        raise ImproperlyConfigured(
            'CAS_CREATE_USER_WITH_ID is True, but no attributes were provided')
    user_id = attributes.get('id')
    if not user_id:
        raise ImproperlyConfigured(
            "CAS_CREATE_USER_WITH_ID is True, but `'id'` is not part of attributes."
            )
    return user_id