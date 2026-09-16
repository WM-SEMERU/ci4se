def model_actions(self, model, **kwargs):
    check(model)
    ctype = ContentType.objects.get_for_model(model)
    return self.public(Q(target_content_type=ctype) | Q(
        action_object_content_type=ctype) | Q(actor_content_type=ctype), **
        kwargs)