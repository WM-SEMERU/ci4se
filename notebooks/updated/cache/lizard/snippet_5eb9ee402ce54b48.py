def print_facilities(self, facilities):
    for facility in facilities:
        print('{} - ({}): {}'.format(facility.code, facility.name, ','.join
            (facility.features)))