def get_for_objects(self, queryset):
    if not isinstance(queryset, QuerySet) or queryset.count() == 0:
        return self.none()
    content_type = ContentType.objects.get_for_model(queryset.model)
    primary_keys = queryset.values_list(queryset.model._meta.pk.name, flat=True
        )
    if isinstance(primary_keys[0], integer_types):
        return self.filter(content_type=content_type).filter(Q(
            object_id__in=primary_keys)).distinct()
    else:
        return self.filter(content_type=content_type).filter(Q(
            object_pk__in=primary_keys)).distinct()