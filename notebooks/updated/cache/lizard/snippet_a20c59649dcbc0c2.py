def get_http_headers(user_agent=None, referer=None, accept_language=None):
    if user_agent is None:
        user_agent = settings.default_user_agent
    if referer is None:
        referer = settings.default_referer
    if accept_language is None:
        accept_language = settings.default_accept_language
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': user_agent, 'referer': referer,
        'Accept-Language': accept_language})
    return headers