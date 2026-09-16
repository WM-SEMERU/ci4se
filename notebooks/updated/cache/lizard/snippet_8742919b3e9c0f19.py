def get_entity_kind(self, model_obj):
    model_obj_ctype = ContentType.objects.get_for_model(self.queryset.model)
    return '{0}.{1}'.format(model_obj_ctype.app_label, model_obj_ctype.model
        ), '{0}'.format(model_obj_ctype)