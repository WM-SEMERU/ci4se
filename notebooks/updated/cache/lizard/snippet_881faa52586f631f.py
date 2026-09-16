def _svrg_grads_update_rule(self, g_curr_batch_curr_weight,
    g_curr_batch_special_weight, g_special_weight_all_batch):
    for index, grad in enumerate(g_curr_batch_curr_weight):
        grad -= g_curr_batch_special_weight[index]
        grad += g_special_weight_all_batch[index]
    return g_curr_batch_curr_weight