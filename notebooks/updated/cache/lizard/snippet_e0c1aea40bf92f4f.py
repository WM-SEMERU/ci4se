def profile_validation(self, status):
    self.selected_profile.data.setdefault('validation_pass_count', 0)
    self.selected_profile.data.setdefault('validation_fail_count', 0)
    if status:
        self.selected_profile.data['validation_pass_count'] += 1
    else:
        self.selected_profile.data['validation_fail_count'] += 1