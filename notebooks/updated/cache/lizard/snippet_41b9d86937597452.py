def get_probability_masks(self, non_valid_value=0):
    if self.probability_masks is None:
        self.get_data()
        self.probability_masks = (self.cloud_detector.
            get_cloud_probability_maps(self.bands))
    self.probability_masks[~self.valid_data] = non_valid_value
    return self.probability_masks