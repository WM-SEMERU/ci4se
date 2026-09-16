def feature_info(self):
    feature_list = self.prop('available-features-list', None)
    if feature_list is None:
        raise ValueError('Firmware features are not supported on CPC %s' %
            self.name)
    return feature_list