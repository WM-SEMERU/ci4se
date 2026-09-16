def get_serializer_context(self):
    context = super(OfficeMixin, self).get_serializer_context()
    context['election_date'] = self.kwargs['date']
    return context