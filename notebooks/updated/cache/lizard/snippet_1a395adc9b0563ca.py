def pre_save_moderation(self, sender, comment, request, **kwargs):
    model = comment.content_type.model_class()
    if model not in self._registry:
        return
    content_object = comment.content_object
    moderation_class = self._registry[model]
    if not moderation_class.allow(comment, content_object, request):
        return False
    if moderation_class.moderate(comment, content_object, request):
        comment.is_public = False