def _get_labels_right(self, validate=None):
    labels = []
    for compare_func in self.features:
        labels = labels + listify(compare_func.labels_right)
    if not is_label_dataframe(labels, validate):
        error_msg = 'label is not found in the dataframe'
        raise KeyError(error_msg)
    return unique(labels)