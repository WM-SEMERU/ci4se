def response_change(self, request, obj):
    if (request.POST and '_continue' not in request.POST and '_saveasnew'
         not in request.POST and '_addanother' not in request.POST):
        if obj.parent:
            url = reverse('admin:filer-directory_listing', kwargs={
                'folder_id': obj.parent.id})
        else:
            url = reverse('admin:filer-directory_listing-root')
        url = '{0}{1}'.format(url, admin_url_params_encoded(request))
        return HttpResponseRedirect(url)
    return super(FolderAdmin, self).response_change(request, obj)