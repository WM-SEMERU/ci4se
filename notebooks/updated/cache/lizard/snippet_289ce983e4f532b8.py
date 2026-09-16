def _get_context_id(self):
    from furious.context import get_current_context
    context_id = self._options.get('context_id')
    if context_id:
        return context_id
    try:
        context = get_current_context()
    except errors.NotInContextError:
        context = None
        self.update_options(context_id=None)
    if context:
        context_id = context.id
        self.update_options(context_id=context_id)
    return context_id