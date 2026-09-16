def transitions(network, before_state, after_state):
    possible_causes = np.where(np.sum(network.cm, 1) > 0)[0]
    possible_effects = np.where(np.sum(network.cm, 0) > 0)[0]
    for cause_subset in utils.powerset(possible_causes, nonempty=True):
        for effect_subset in utils.powerset(possible_effects, nonempty=True):
            try:
                yield Transition(network, before_state, after_state,
                    cause_subset, effect_subset)
            except exceptions.StateUnreachableError:
                pass