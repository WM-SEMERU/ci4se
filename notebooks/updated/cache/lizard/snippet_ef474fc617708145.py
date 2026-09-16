def _combine_activations(layer1, layer2, activations1=None, activations2=
    None, mode=ActivationTranslation.BIDIRECTIONAL, number_activations=
    NUMBER_OF_AVAILABLE_SAMPLES):
    activations1 = activations1 or layer1.activations[:number_activations,
        (...)]
    activations2 = activations2 or layer2.activations[:number_activations,
        (...)]
    if mode is ActivationTranslation.ONE_TO_TWO:
        acts_1_to_2 = push_activations(activations1, layer1, layer2)
        return acts_1_to_2, activations2
    elif mode is ActivationTranslation.BIDIRECTIONAL:
        acts_1_to_2 = push_activations(activations1, layer1, layer2)
        acts_2_to_1 = push_activations(activations2, layer2, layer1)
        activations_model1 = np.concatenate((activations1, acts_1_to_2), axis=1
            )
        activations_model2 = np.concatenate((acts_2_to_1, activations2), axis=1
            )
        return activations_model1, activations_model2