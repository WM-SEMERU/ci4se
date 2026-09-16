def dataset_detail(request, dataset_id):
    active_dataset = get_object_or_404(Dataset, pk=dataset_id)
    datadict_id = active_dataset.data_dictionary_id
    datadict = DataDictionaryField.objects.filter(parent_dict=datadict_id
        ).order_by('columnIndex')
    uploader_name = grab_names_from_emails([active_dataset.uploaded_by])
    tags = Tag.objects.filter(dataset=dataset_id)
    articles = Article.objects.filter(dataset=dataset_id)
    for hub in HUBS_LIST:
        if hub['slug'] == active_dataset.hub_slug:
            active_dataset.hub = hub['name']
            active_dataset.vertical = hub['vertical']['name']
    if len(uploader_name) == 0:
        uploader_name = active_dataset.uploaded_by
    else:
        uploader_name = uploader_name[active_dataset.uploaded_by]
    return render(request, 'datafreezer/dataset_details.html', {'dataset':
        active_dataset, 'datadict': datadict, 'uploader_name':
        uploader_name, 'tags': tags, 'articles': articles})