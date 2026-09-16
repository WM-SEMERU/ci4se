def store_transition(self, frame, action, reward, done, extra_info=None):
    self.current_idx = (self.current_idx + 1) % self.buffer_capacity
    self.state_buffer[self.current_idx] = frame
    self.action_buffer[self.current_idx] = action
    self.reward_buffer[self.current_idx] = reward
    self.dones_buffer[self.current_idx] = done
    for name in self.extra_data:
        self.extra_data[name][self.current_idx] = extra_info[name]
    if self.current_size < self.buffer_capacity:
        self.current_size += 1
    return self.current_idx