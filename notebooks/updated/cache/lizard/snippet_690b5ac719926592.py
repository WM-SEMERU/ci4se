def _yellowfin(self):
    yellowfin_ops = []
    curv_range_ops = self._curvature_range()
    yellowfin_ops += curv_range_ops
    grad_var_ops = self._grad_variance()
    yellowfin_ops += grad_var_ops
    dist_to_opt_ops = self._dist_to_opt()
    yellowfin_ops += dist_to_opt_ops
    self._mu = tf.identity(tf.cond(self._do_tune, self._get_mu_tensor, lambda :
        self._mu_var))
    with tf.control_dependencies([self._mu]):
        self._lr = tf.identity(tf.cond(self._do_tune, self._get_lr_tensor, 
            lambda : self._lr_var))
    with tf.control_dependencies([self._mu, self._lr]):
        self._mu = self._beta * self._mu_var + (1 - self._beta) * self._mu
        self._lr = self._beta * self._lr_var + (1 - self._beta) * self._lr
        yellowfin_ops.append(tf.assign(self._mu_var, self._mu))
        yellowfin_ops.append(tf.assign(self._lr_var, self._lr))
    yellowfin_ops = tf.group(*yellowfin_ops)
    return yellowfin_ops