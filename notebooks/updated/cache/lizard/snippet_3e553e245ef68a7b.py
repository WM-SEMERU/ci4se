def aggregate_grads(all_grads, colocation=False, devices=None, average=True):
    assert not (devices is not None and colocation)
    if devices is not None:
        assert isinstance(devices, list), devices
    nr_tower = len(all_grads)
    if nr_tower == 1:
        return all_grads[0]

    def aggregate(grads):
        if average:
            return tf.multiply(tf.add_n(grads), 1.0 / nr_tower)
        else:
            return tf.add_n(grads)
    ret = []
    for idx, grad_and_vars in enumerate(zip(*all_grads)):
        v = grad_and_vars[0][1]
        grads = [g for g, _ in grad_and_vars]
        if colocation:
            with tf.device(v.device):
                grad = aggregate(grads)
        elif devices is None:
            grad = aggregate(grads)
        else:
            dev = devices[idx % len(devices)]
            with tf.device(dev):
                grad = aggregate(grads)
        ret.append((grad, v))
    return ret