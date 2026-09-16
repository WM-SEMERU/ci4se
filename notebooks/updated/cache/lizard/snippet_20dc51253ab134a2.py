def generate_matching_datasets(self, data_slug):
    matching_hubs = VERTICAL_HUB_MAP[data_slug]['hubs']
    return Dataset.objects.filter(hub_slug__in=matching_hubs)