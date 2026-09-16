def get_countries(self):
    qs = Venue.objects.values('country').exclude(country='').distinct(
        ).order_by('country')
    countries = []
    for c in qs:
        countries.append({'code': c['country'], 'name': Venue.
            get_country_name(c['country'])})
    return sorted(countries, key=lambda k: k['name'])