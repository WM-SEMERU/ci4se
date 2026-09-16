def _compile_to_sklearn(self, expr):
    sklearn_pipeline_str = generate_pipeline_code(expr_to_tree(expr, self.
        _pset), self.operators)
    sklearn_pipeline = eval(sklearn_pipeline_str, self.operators_context)
    sklearn_pipeline.memory = self._memory
    return sklearn_pipeline