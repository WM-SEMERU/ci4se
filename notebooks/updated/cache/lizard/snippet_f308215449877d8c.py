def get_pandasframe(self):
    if self.dataset:
        self._load_dimensions()
        return self._get_pandasframe_one_dataset()
    return self._get_pandasframe_across_datasets()