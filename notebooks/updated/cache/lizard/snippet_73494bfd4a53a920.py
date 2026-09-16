def run(self, conf, arg, err):
    weld_context_new = weld.weld_context_new
    weld_context_new.argtypes = [c_weld_conf]
    weld_context_new.restype = c_weld_context
    ctx = weld_context_new(conf.conf)
    weld_module_run = weld.weld_module_run
    weld_module_run.argtypes = [c_weld_module, c_weld_context, c_weld_value,
        c_weld_err]
    weld_module_run.restype = c_weld_value
    ret = weld_module_run(self.module, ctx, arg.val, err.error)
    return WeldValue(ret, assign=True, _ctx=ctx)