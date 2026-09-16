def delete_custom_public_read_api(request, database_name, collection_name, slug
    ):
    ss = get_object_or_404(CustomPublicReadAPI, datbase_name=database_name,
        collection_name=collection_name, slug=slug)
    ss.delete()
    messages.success(request, _('Custom Public Read API deleted.'))
    return HttpResponseRedirect(reverse('djmongo_show_apis', args=(ss.
        database_name, ss.collection_name)))