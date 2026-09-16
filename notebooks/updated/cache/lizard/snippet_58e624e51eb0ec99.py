def _get_auth_challenge(self, exc):
    response = HttpResponse(content=exc.content, status=exc.get_code_num())
    response['WWW-Authenticate'] = 'Basic realm="%s"' % REALM
    return response