def page_location(self):
    cycle = self.election_day.cycle.name
    if self.content_type.model_class() == PageType:
        print(self.content_object)
        return self.content_object.page_location_template()
    elif self.content_type.model_class() == Division:
        if self.content_object.level.name == DivisionLevel.STATE:
            if self.special_election:
                path = os.path.join(self.content_object.slug,
                    'special-election', self.election_day.
                    special_election_datestring())
            else:
                path = self.content_object.slug
        else:
            path = ''
    elif self.division.level.name == DivisionLevel.STATE:
        if not self.content_object.body:
            path = os.path.join(self.division.slug, 'governor')
        else:
            path = os.path.join(self.division.slug, self.content_object.slug)
    else:
        path = self.content_object.slug
    return os.sep + os.path.normpath(os.path.join(cycle, path)) + os.sep