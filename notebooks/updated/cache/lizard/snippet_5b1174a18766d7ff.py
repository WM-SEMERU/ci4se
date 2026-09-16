def to_dict(self):
    return {'model_type': 'segmented_regression', 'name': self.name,
        'segmentation_col': self.segmentation_col, 'fit_filters': self.
        fit_filters, 'predict_filters': self.predict_filters,
        'min_segment_size': self.min_segment_size, 'default_config': {
        'model_expression': self.default_model_expr, 'ytransform':
        YTRANSFORM_MAPPING[self.default_ytransform]}, 'fitted': self.fitted,
        'models': {yamlio.to_scalar_safe(name): self._process_model_dict(m.
        to_dict()) for name, m in self._group.models.items()}}