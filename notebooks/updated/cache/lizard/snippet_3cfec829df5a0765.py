def load_profile(self, profile):
    profile_path = os.path.join(self.root_directory, 'minimum_needs', 
        profile + '.json')
    self.read_from_file(profile_path)