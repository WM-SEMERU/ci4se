def init_nautilus(method):
    print('Preference elicitation options:')
    print('\t1 - Percentages')
    print('\t2 - Relative ranks')
    print('\t3 - Direct')
    PREFCLASSES = [PercentageSpecifictation, RelativeRanking,
        DirectSpecification]
    pref_sel = int(_prompt_wrapper('Reference elicitation ', default='%s' %
        1, validator=NumberValidator([1, 3])))
    preference_class = PREFCLASSES[pref_sel - 1]
    print('Nadir: %s' % method.problem.nadir)
    print('Ideal: %s' % method.problem.ideal)
    if method.current_iter - method.user_iters:
        finished_iter = method.user_iters - method.current_iter
    else:
        finished_iter = 0
    new_iters = int(_prompt_wrapper('Ni: ', default='%s' % method.
        current_iter, validator=NumberValidator()))
    method.current_iter = new_iters
    method.user_iters = finished_iter + new_iters
    return preference_class