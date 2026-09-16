def compute_gradients(self, loss, var_list, global_step=None,
    gate_gradients=GATE_OP, aggregation_method=None,
    colocate_gradients_with_ops=False, name=None, grad_loss=None):
    del global_step, name
    return self._momentum_optimizer.compute_gradients(loss, var_list=
        var_list, gate_gradients=gate_gradients, aggregation_method=
        aggregation_method, colocate_gradients_with_ops=
        colocate_gradients_with_ops, grad_loss=grad_loss)