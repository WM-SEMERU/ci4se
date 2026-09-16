def list_managers_view(request):
    managerset = Manager.objects.filter(active=True)
    return render_to_response('list_managers.html', {'page_name':
        'Managers', 'managerset': managerset}, context_instance=
        RequestContext(request))