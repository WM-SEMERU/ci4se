def get_domain_id_for_operation(request):
    domain_context = request.session.get('domain_context')
    if domain_context:
        return domain_context
    return api.keystone.get_effective_domain_id(request)