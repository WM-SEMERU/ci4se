def _l_cv_weight_factor(self):
    b = 0.0047 * sqrt(0) + 0.0023 / 2
    c = 0.02609 / (self.catchment.record_length - 1)
    return c / (b + c)