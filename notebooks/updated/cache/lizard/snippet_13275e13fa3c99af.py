def analyze(self, M_c, T, X_L, X_D, seed, kernel_list=(), n_steps=1, c=(),
    r=(), max_iterations=-1, max_time=-1, do_diagnostics=False,
    diagnostics_every_N=1, ROW_CRP_ALPHA_GRID=(), COLUMN_CRP_ALPHA_GRID=(),
    S_GRID=(), MU_GRID=(), N_GRID=31, do_timing=False, CT_KERNEL=0,
    progress=None):
    if n_steps <= 0:
        raise ValueError('You must do at least one analyze step.')
    if CT_KERNEL not in [0, 1]:
        raise ValueError('CT_KERNEL must be 0 (Gibbs) or 1 (MH)')
    if do_timing:
        do_diagnostics = False
    diagnostic_func_dict, reprocess_diagnostics_func = (
        do_diagnostics_to_func_dict(do_diagnostics))
    X_L_list, X_D_list, was_multistate = su.ensure_multistate(X_L, X_D)
    arg_tuples = self.get_analyze_arg_tuples(M_c, T, X_L_list, X_D_list,
        kernel_list, n_steps, c, r, max_iterations, max_time,
        diagnostic_func_dict, diagnostics_every_N, ROW_CRP_ALPHA_GRID,
        COLUMN_CRP_ALPHA_GRID, S_GRID, MU_GRID, N_GRID, do_timing,
        CT_KERNEL, progress, make_get_next_seed(seed))
    chain_tuples = self.mapper(self.do_analyze, arg_tuples)
    X_L_list, X_D_list, diagnostics_dict_list = zip(*chain_tuples)
    if do_timing:
        timing_list = diagnostics_dict_list
    if not was_multistate:
        X_L_list, X_D_list = X_L_list[0], X_D_list[0]
    ret_tuple = X_L_list, X_D_list
    if diagnostic_func_dict is not None:
        diagnostics_dict = munge_diagnostics(diagnostics_dict_list)
        if reprocess_diagnostics_func is not None:
            diagnostics_dict = reprocess_diagnostics_func(diagnostics_dict)
        ret_tuple = ret_tuple + (diagnostics_dict,)
    if do_timing:
        ret_tuple = ret_tuple + (timing_list,)
    return ret_tuple