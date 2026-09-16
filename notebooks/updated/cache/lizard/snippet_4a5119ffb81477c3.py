def _get_scheduler(self, net, policy, **scheduler_kwargs):
    if policy not in [CyclicLR, ReduceLROnPlateau
        ] and 'last_epoch' not in scheduler_kwargs:
        last_epoch = len(net.history) - 1
        scheduler_kwargs['last_epoch'] = last_epoch
    if policy is CyclicLR and 'last_batch_idx' not in scheduler_kwargs:
        scheduler_kwargs['last_batch_idx'] = self.batch_idx_ - 1
    return policy(net.optimizer_, **scheduler_kwargs)