def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    can_delete = True
    protected_objects = []
    collector_message = None
    collector = Collector(using='default')
    try:
        collector.collect([self.object])
    except ProtectedError as e:
        collector_message = (
            'Cannot delete %s because it has relations that depends on it.' %
            self.object)
        protected_objects = e.protected_objects
        can_delete = False
    if can_delete and self.redirect:
        messages.success(request, self.get_success_message(self.object))
        return self.delete(request, *args, **kwargs)
    context = self.get_context_data(object=self.object, can_delete=
        can_delete, collector_message=collector_message, protected_objects=
        protected_objects)
    return self.render_to_response(context)