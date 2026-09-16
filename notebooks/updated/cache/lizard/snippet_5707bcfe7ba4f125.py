def get_device_category(self, cat):
    if cat in self.device_categories:
        return self.device_categories[cat]
    else:
        return False