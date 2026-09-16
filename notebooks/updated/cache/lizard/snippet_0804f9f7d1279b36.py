def soft_target_update(self):
    for target_param, local_param in zip(self.target.parameters(), self.
        local.parameters()):
        target_param.data.copy_(self.tau * local_param.data + (1.0 - self.
            tau) * target_param.data)