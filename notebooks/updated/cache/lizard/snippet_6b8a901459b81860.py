def generate_additional_context(self, matching_datasets):
    dataset_ids = [upload.id for upload in matching_datasets]
    tags = Tag.objects.filter(dataset__in=dataset_ids).distinct().annotate(
        Count('word')).order_by('-word__count')[:5]
    hubs = matching_datasets.values('hub_slug').annotate(Count('hub_slug')
        ).order_by('-hub_slug__count')
    if hubs:
        most_used_hub = get_hub_name_from_slug(hubs[0]['hub_slug'])
        hub_slug = hubs[0]['hub_slug']
    else:
        most_used_hub = None
        hub_slug = None
    return {'tags': tags, 'hub': most_used_hub, 'hub_slug': hub_slug}