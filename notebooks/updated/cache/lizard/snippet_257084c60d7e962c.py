def get_jwt_value(self, request):
    from django.utils.encoding import smart_text
    from django.utils.translation import ugettext as _
    from rest_framework import exceptions
    auth = self.get_authorization(request).split()
    auth_header_prefix = self.prefix.lower() or ''
    if not auth:
        if self.cookie:
            return request.COOKIES.get(self.cookie)
        return None
    if auth_header_prefix is None or len(auth_header_prefix) < 1:
        auth.append('')
        auth.reverse()
    if smart_text(auth[0].lower()) != auth_header_prefix:
        return None
    if len(auth) == 1:
        msg = _('Invalid Authorization header. No credentials provided.')
        raise exceptions.AuthenticationFailed(msg)
    elif len(auth) > 2:
        msg = _(
            'Invalid Authorization header. Credentials string should not contain spaces.'
            )
        raise exceptions.AuthenticationFailed(msg)
    return auth[1]