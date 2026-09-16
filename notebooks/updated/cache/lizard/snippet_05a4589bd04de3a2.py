def workflow_states_column(self, obj):
    workflow_states = models.WorkflowState.objects.filter(content_type=self
        ._get_obj_ct(obj), object_id=obj.pk)
    return ', '.join([unicode(wfs) for wfs in workflow_states])