def to_dict(self):
    return {'model_type': 'segmented_discretechoice', 'name': self.name,
        'segmentation_col': self.segmentation_col, 'sample_size': self.
        sample_size, 'probability_mode': self.probability_mode,
        'choice_mode': self.choice_mode, 'choosers_fit_filters': self.
        choosers_fit_filters, 'choosers_predict_filters': self.
        choosers_predict_filters, 'alts_fit_filters': self.alts_fit_filters,
        'alts_predict_filters': self.alts_predict_filters,
        'interaction_predict_filters': self.interaction_predict_filters,
        'estimation_sample_size': self.estimation_sample_size,
        'prediction_sample_size': self.prediction_sample_size,
        'choice_column': self.choice_column, 'default_config': {
        'model_expression': self.default_model_expr}, 'remove_alts': self.
        remove_alts, 'fitted': self.fitted, 'models': {yamlio.
        to_scalar_safe(name): self._process_model_dict(m.to_dict()) for 
        name, m in self._group.models.items()}}