def get_serializer_context(self):
    context = super(StateMixin, self).get_serializer_context()
    context['election_date'] = self.kwargs['date']
    return context