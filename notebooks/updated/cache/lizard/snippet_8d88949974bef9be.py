def _expand_shorthand(model_formula, variables):
    wm = 'white_matter'
    gsr = 'global_signal'
    rps = 'trans_x + trans_y + trans_z + rot_x + rot_y + rot_z'
    fd = 'framewise_displacement'
    acc = _get_matches_from_data('a_comp_cor_[0-9]+', variables)
    tcc = _get_matches_from_data('t_comp_cor_[0-9]+', variables)
    dv = _get_matches_from_data('^std_dvars$', variables)
    dvall = _get_matches_from_data('.*dvars', variables)
    nss = _get_matches_from_data('non_steady_state_outlier[0-9]+', variables)
    spikes = _get_matches_from_data('motion_outlier[0-9]+', variables)
    model_formula = re.sub('wm', wm, model_formula)
    model_formula = re.sub('gsr', gsr, model_formula)
    model_formula = re.sub('rps', rps, model_formula)
    model_formula = re.sub('fd', fd, model_formula)
    model_formula = re.sub('acc', acc, model_formula)
    model_formula = re.sub('tcc', tcc, model_formula)
    model_formula = re.sub('dv', dv, model_formula)
    model_formula = re.sub('dvall', dvall, model_formula)
    model_formula = re.sub('nss', nss, model_formula)
    model_formula = re.sub('spikes', spikes, model_formula)
    formula_variables = _get_variables_from_formula(model_formula)
    others = ' + '.join(set(variables) - set(formula_variables))
    model_formula = re.sub('others', others, model_formula)
    return model_formula