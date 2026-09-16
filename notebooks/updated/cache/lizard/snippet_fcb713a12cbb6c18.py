def directly_related(obj, count, collected_so_far, mods=[],
    only_from_same_site=True):
    qset = Related.objects.filter(publishable=obj)
    if mods:
        qset = qset.filter(related_ct__in=[ContentType.objects.
            get_for_model(m).pk for m in mods])
    return get_cached_objects(qset.values_list('related_ct', 'related_id')[
        :count], missing=SKIP)