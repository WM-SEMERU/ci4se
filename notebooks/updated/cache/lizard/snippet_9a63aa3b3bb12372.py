def __calculate_boltzmann_factor(self, state_key, next_action_list):
    sigmoid = self.__calculate_sigmoid()
    q_df = self.q_df[self.q_df.state_key == state_key]
    q_df = q_df[q_df.isin(next_action_list)]
    q_df['boltzmann_factor'] = q_df['q_value'] / sigmoid
    q_df['boltzmann_factor'] = q_df['boltzmann_factor'].apply(np.exp)
    q_df['boltzmann_factor'] = q_df['boltzmann_factor'] / q_df[
        'boltzmann_factor'].sum()
    return q_df