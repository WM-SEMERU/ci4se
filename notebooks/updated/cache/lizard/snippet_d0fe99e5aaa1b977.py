def get_poll_option_formset_kwargs(self):
    kwargs = {'prefix': 'poll'}
    if self.request.method in ('POST', 'PUT'):
        kwargs.update({'data': self.request.POST, 'files': self.request.FILES})
    else:
        topic = self.get_topic()
        poll_option_queryset = TopicPollOption.objects.filter(poll__topic=topic
            )
        kwargs.update({'queryset': poll_option_queryset})
    return kwargs