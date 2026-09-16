def remove_profile(self, profile):
    self.remove_file(os.path.join(self.root_directory, 'minimum_needs', 
        profile + '.json'))