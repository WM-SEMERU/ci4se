def profile_execution(self, status):
    self.selected_profile.data['execution_success'] = status
    if status:
        self.report['results']['executions']['pass'] += 1
    else:
        self.report['results']['executions']['fail'] += 1
        if self.selected_profile.name not in self.report['results'][
            'failed_profiles']:
            self.report['results']['failed_profiles'].append(self.
                selected_profile.name)