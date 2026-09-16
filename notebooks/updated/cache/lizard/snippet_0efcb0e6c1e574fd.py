def _decay(self):
    if self.decay_cost is not None:
        return self.decay_cost
    costs = []
    if self.device_name is None:
        for var in tf.trainable_variables():
            if var.op.name.find('DW') > 0:
                costs.append(tf.nn.l2_loss(var))
    else:
        for layer in self.layers:
            for var in layer.params_device[self.device_name].values():
                if isinstance(var, tf.Variable) and var.op.name.find('DW') > 0:
                    costs.append(tf.nn.l2_loss(var))
    self.decay_cost = tf.multiply(self.hps.weight_decay_rate, tf.add_n(costs))
    return self.decay_cost