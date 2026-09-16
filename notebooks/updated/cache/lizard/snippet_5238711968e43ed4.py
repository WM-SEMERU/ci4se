def AfterTransitionEventHandler(instance, event):
    if call_workflow_event(instance, event, after=True):
        return
    if not event.transition:
        return
    if skip(instance, event.transition.id):
        return
    instance.reindexObject()
    key = 'after_{0}_transition_event'.format(event.transition.id)
    after_event = getattr(instance, key, False)
    if not after_event:
        key = 'workflow_script_' + event.transition.id
        after_event = getattr(instance, key, False)
    if not after_event:
        return
    after_event()