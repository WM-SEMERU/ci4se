def stack_decon_stims(stim_list):
    stim_names = list(set(nl.flatten([stims.keys() for stims in stim_list])))
    stim_dict = {}
    for stim_name in stim_names:
        types = list(set([stims[stim_name].type() for stims in stim_list if
            stim_name in stims]))
        if len(types) > 1:
            nl.notify(
                'Error: Trying to stack stimuli of different types! (%s)' %
                stim_name, level=nl.level.error)
            return None
        type = types[0]
        stim_stack = []
        for i in xrange(len(stim_list)):
            if stim_name in stim_list[i]:
                stim_stack.append(stim_list[i][stim_name])
            else:
                stim_stack.append(stim_list[i].values()[0].blank_stim(type=
                    type))
        stim_dict[stim_name] = copy.copy(stim_stack[0])
        for stim in stim_stack[1:]:
            stim_dict[stim_name] = stim_dict[stim_name].concat_stim(stim)
    return stim_dict.values()