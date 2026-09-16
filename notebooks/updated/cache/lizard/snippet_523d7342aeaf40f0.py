def create_observation_streams(self, num_streams, h_size, num_layers):
    brain = self.brain
    activation_fn = self.swish
    self.visual_in = []
    for i in range(brain.number_visual_observations):
        visual_input = self.create_visual_input(brain.camera_resolutions[i],
            name='visual_observation_' + str(i))
        self.visual_in.append(visual_input)
    vector_observation_input = self.create_vector_input()
    final_hiddens = []
    for i in range(num_streams):
        visual_encoders = []
        hidden_state, hidden_visual = None, None
        if self.vis_obs_size > 0:
            for j in range(brain.number_visual_observations):
                encoded_visual = self.create_visual_observation_encoder(self
                    .visual_in[j], h_size, activation_fn, num_layers,
                    'main_graph_{}_encoder{}'.format(i, j), False)
                visual_encoders.append(encoded_visual)
            hidden_visual = tf.concat(visual_encoders, axis=1)
        if brain.vector_observation_space_size > 0:
            hidden_state = self.create_vector_observation_encoder(
                vector_observation_input, h_size, activation_fn, num_layers,
                'main_graph_{}'.format(i), False)
        if hidden_state is not None and hidden_visual is not None:
            final_hidden = tf.concat([hidden_visual, hidden_state], axis=1)
        elif hidden_state is None and hidden_visual is not None:
            final_hidden = hidden_visual
        elif hidden_state is not None and hidden_visual is None:
            final_hidden = hidden_state
        else:
            raise Exception(
                'No valid network configuration possible. There are no states or observations in this brain'
                )
        final_hiddens.append(final_hidden)
    return final_hiddens