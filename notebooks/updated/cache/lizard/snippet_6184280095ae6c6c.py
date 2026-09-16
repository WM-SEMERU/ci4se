def api_techgroup_list(request, key, hproPk):
    if not check_api_key(request, key, hproPk):
        return HttpResponseForbidden
    from users.models import TechGroup
    retour = [{'uuid': t.uuid, 'uid': t.uid, 'name': t.name} for t in
        TechGroup.objects.filter(is_enabled=True)]
    return HttpResponse(json.dumps(retour), content_type='application/json')