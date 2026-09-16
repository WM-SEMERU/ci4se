def find_path_with_profiles(self, conversion_profiles, in_, out):
    original_profiles = dict(self.conversion_profiles)
    self._setup_profiles(conversion_profiles)
    results = self.find_path(in_, out)
    self.conversion_profiles = original_profiles
    return results