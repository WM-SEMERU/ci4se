def render(self, data, accepted_media_type=None, renderer_context=None):
    wrapper = None
    success = False
    for wrapper_name in self.wrappers:
        wrapper_method = getattr(self, wrapper_name)
        try:
            wrapper = wrapper_method(data, renderer_context)
        except WrapperNotApplicable:
            pass
        else:
            success = True
            break
    if not success:
        raise WrapperNotApplicable('No acceptable wrappers found for response.'
            , data=data, renderer_context=renderer_context)
    renderer_context['indent'] = 4
    return super(JsonApiMixin, self).render(data=wrapper,
        accepted_media_type=accepted_media_type, renderer_context=
        renderer_context)