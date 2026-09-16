def get_post_authorization_redirect_url(request, canvas=True):
    path = request.get_full_path()
    if canvas:
        if FACEBOOK_APPLICATION_CANVAS_URL:
            path = path.replace(urlparse(FACEBOOK_APPLICATION_CANVAS_URL).
                path, '')
        redirect_uri = 'https://%(domain)s/%(namespace)s%(path)s' % {'domain':
            FACEBOOK_APPLICATION_DOMAIN, 'namespace':
            FACEBOOK_APPLICATION_NAMESPACE, 'path': path}
    else:
        if FANDJANGO_SITE_URL:
            site_url = FANDJANGO_SITE_URL
            path = path.replace(urlparse(site_url).path, '')
        else:
            protocol = 'https' if request.is_secure() else 'http'
            site_url = '%s://%s' % (protocol, request.get_host())
        redirect_uri = site_url + path
    return redirect_uri