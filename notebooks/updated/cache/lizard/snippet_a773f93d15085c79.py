def _render(self, data, formula_def):
    renderer = formula_def.get('renderer', self.opts.get('renderer',
        'jinja|yaml'))
    rend = salt.loader.render(self.opts, {})
    blacklist = self.opts.get('renderer_blacklist')
    whitelist = self.opts.get('renderer_whitelist')
    template_vars = formula_def.copy()
    template_vars['opts'] = self.opts.copy()
    return compile_template(':string:', rend, renderer, blacklist,
        whitelist, input_data=data, **template_vars)