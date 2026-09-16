def add_pool_view(request, semester):
    page_name = 'Add Workshift Pool'
    add_pool_form = PoolForm(data=request.POST or None, semester=semester,
        full_management=True)
    if add_pool_form.is_valid():
        add_pool_form.save()
        messages.add_message(request, messages.INFO, 'Workshift pool added.')
        return HttpResponseRedirect(wurl('workshift:manage', sem_url=
            semester.sem_url))
    return render_to_response('add_pool.html', {'page_name': page_name,
        'add_pool_form': add_pool_form}, context_instance=RequestContext(
        request))