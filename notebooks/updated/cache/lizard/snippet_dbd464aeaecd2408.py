def expert_to_gates(self):
    return self._ep(tf.concat, transpose_list_of_lists(self._dp(lambda d: d
        .expert_to_gates(), self._dispatchers)), 0)