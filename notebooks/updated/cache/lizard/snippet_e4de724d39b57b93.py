def filename_patterns(self):
    patterns = []
    for directory in self.base_directories:
        patterns.append(self.get_main_pattern(directory))
        patterns.append(self.get_modular_pattern(directory))
    return patterns