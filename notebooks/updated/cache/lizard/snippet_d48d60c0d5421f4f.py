def re_pipe(FlowRate, Diam, Nu):
    ut.check_range([FlowRate, '>0', 'Flow rate'], [Diam, '>0', 'Diameter'],
        [Nu, '>0', 'Nu'])
    return 4 * FlowRate / (np.pi * Diam * Nu)