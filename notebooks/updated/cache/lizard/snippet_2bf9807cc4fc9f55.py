def eval_js(self, expr):
    if not self.is_built():
        self._pending_js_eval.append(expr)
        return
    logger.log(5, 'Evaluate Javascript: `%s`.', expr)
    out = self.page().mainFrame().evaluateJavaScript(expr)
    return _to_py(out)