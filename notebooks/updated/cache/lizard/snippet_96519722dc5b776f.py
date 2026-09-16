def transform_string(self, jsx, harmony=False, strip_types=False):
    opts = {'harmony': harmony, 'stripTypes': strip_types}
    try:
        result = self.context.call('%s.transform' % self.
            JSX_TRANSFORMER_JS_EXPR, jsx, opts)
    except execjs.ProgramError as e:
        raise TransformError(str(e))
    js = result['code']
    return js