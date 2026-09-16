def columns_used(self):
    return list(tz.unique(tz.concatv(self.choosers_columns_used(), self.
        alts_columns_used(), self.interaction_columns_used(), util.
        columns_in_formula(self.default_model_expr), [self.segmentation_col])))