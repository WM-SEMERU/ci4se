def query_module_funcs(self, module):
    funcs = self.session.query(Export).filter_by(module=module).all()
    return funcs