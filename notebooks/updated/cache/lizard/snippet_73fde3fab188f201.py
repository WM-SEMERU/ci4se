def apply_optimization(self, update_embedding_with, grad, **kwargs):
    if self.linesearch:
        return self._apply_linesearch_optimzation(update_embedding_with,
            grad, **kwargs)
    else:
        return self._apply_fixed_optimization(update_embedding_with, grad,
            **kwargs)