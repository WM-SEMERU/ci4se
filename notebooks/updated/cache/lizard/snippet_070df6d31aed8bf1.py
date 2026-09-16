def setup(self, steps=None, drop_na=False, **kwargs):
    input_nodes = None
    selectors = self.model.get('input', {}).copy()
    selectors.update(kwargs)
    for i, b in enumerate(self.steps):
        if steps is not None and i not in steps and b.name not in steps:
            continue
        b.setup(input_nodes, drop_na=drop_na, **selectors)
        input_nodes = b.output_nodes