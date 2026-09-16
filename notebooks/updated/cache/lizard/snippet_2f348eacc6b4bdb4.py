def get_elections(self, obj):
    election_day = ElectionDay.objects.get(date=self.context['election_date'])
    kwargs = {'race__office__body': obj, 'election_day': election_day}
    if self.context.get('division') and obj.slug == 'senate':
        kwargs['division'] = self.context['division']
    elif self.context.get('division') and obj.slug == 'house':
        kwargs['division__parent'] = self.context['division']
    if obj.slug == 'house' and not self.context.get('division'):
        kwargs['race__special'] = False
    elections = Election.objects.filter(**kwargs)
    return ElectionSerializer(elections, many=True).data