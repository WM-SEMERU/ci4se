def get_bodies(self, obj):
    return reverse('electionnight_api_body-election-list', request=self.
        context['request'], kwargs={'date': obj.date})