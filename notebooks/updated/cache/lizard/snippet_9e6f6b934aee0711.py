def get_auth_params_from_request(request):
    return (request.user.username, request.user.token.id, request.user.
        tenant_id, request.user.token.project.get('domain_id'), base.
        url_for(request, 'compute'), base.url_for(request, 'identity'))