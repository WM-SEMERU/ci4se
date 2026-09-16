def create_relation(self, calendar, content_object, distinction='',
    inheritable=True):
    return CalendarRelation.objects.create(calendar=calendar, distinction=
        distinction, content_object=content_object)