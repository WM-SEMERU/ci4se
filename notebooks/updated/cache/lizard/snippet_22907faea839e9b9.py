def get_beta(self, kl_loss=0.0):
    if self.hparams.latent_loss_multiplier_dynamic:
        beta = tf.Variable(self.hparams.latent_loss_multiplier, trainable=
            False, dtype=tf.float32)
        alpha = self.hparams.latent_loss_multiplier_alpha
        epsilon = self.hparams.latent_loss_multiplier_epsilon
        shadow_beta = beta + alpha * (kl_loss - epsilon)
        shadow_beta = tf.maximum(shadow_beta, 0.0)
        shadow_beta = tf.minimum(shadow_beta, 1.0)
        update_op = tf.assign(beta, shadow_beta)
    else:
        beta = common_video.beta_schedule(schedule=self.hparams.
            latent_loss_multiplier_schedule, global_step=self.
            get_iteration_num(), final_beta=self.hparams.
            latent_loss_multiplier, decay_start=self.hparams.
            num_iterations_1st_stage + self.hparams.
            num_iterations_2nd_stage, decay_end=self.hparams.anneal_end)
        update_op = tf.identity(beta)
    with tf.control_dependencies([update_op]):
        tf.summary.scalar('beta', beta)
        return beta