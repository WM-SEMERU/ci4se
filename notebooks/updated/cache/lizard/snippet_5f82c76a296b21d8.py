def get_user_id(self, user):
    user_field = getattr(settings, 'SAML_IDP_DJANGO_USERNAME_FIELD', None
        ) or getattr(user, 'USERNAME_FIELD', 'username')
    return str(getattr(user, user_field))