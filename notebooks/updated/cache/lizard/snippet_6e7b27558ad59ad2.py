def get_intrinsic_rewards(self, curr_info, next_info):
    if self.use_curiosity:
        if len(curr_info.agents) == 0:
            return []
        feed_dict = {self.model.batch_size: len(next_info.
            vector_observations), self.model.sequence_length: 1}
        if self.use_continuous_act:
            feed_dict[self.model.selected_actions
                ] = next_info.previous_vector_actions
        else:
            feed_dict[self.model.action_holder
                ] = next_info.previous_vector_actions
        for i in range(self.model.vis_obs_size):
            feed_dict[self.model.visual_in[i]] = curr_info.visual_observations[
                i]
            feed_dict[self.model.next_visual_in[i]
                ] = next_info.visual_observations[i]
        if self.use_vec_obs:
            feed_dict[self.model.vector_in] = curr_info.vector_observations
            feed_dict[self.model.next_vector_in
                ] = next_info.vector_observations
        if self.use_recurrent:
            if curr_info.memories.shape[1] == 0:
                curr_info.memories = self.make_empty_memory(len(curr_info.
                    agents))
            feed_dict[self.model.memory_in] = curr_info.memories
        intrinsic_rewards = self.sess.run(self.model.intrinsic_reward,
            feed_dict=feed_dict) * float(self.has_updated)
        return intrinsic_rewards
    else:
        return None