def _set_categories(self):
    for column, _ in self._categories.items():
        if column in self.columns:
            self[column] = self[column].astype('category')