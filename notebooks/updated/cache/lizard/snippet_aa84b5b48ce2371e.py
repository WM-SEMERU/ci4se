def do_eval(self, inputs, ctx):
    return cwltool.expression.do_eval(self.expr, inputs, self.req, None,
        None, {}, context=ctx)