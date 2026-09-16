def report_validation(self, status):
    if status:
        self.report['results']['validations']['pass'] += 1
    else:
        self.report['results']['validations']['fail'] += 1
        if self.selected_profile.name not in self.report['results'][
            'failed_profiles']:
            self.report['results']['failed_profiles'].append(self.
                selected_profile.name)