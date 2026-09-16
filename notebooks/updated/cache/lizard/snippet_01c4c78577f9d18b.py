def _build_likelihood(self):
    err, nu, Luu, L, alpha, beta, gamma = self._build_common_terms()
    mahalanobisTerm = -0.5 * tf.reduce_sum(tf.square(err) / tf.expand_dims(
        nu, 1)) + 0.5 * tf.reduce_sum(tf.square(gamma))
    constantTerm = -0.5 * self.num_data * tf.log(tf.constant(2.0 * np.pi,
        settings.float_type))
    logDeterminantTerm = -0.5 * tf.reduce_sum(tf.log(nu)) - tf.reduce_sum(tf
        .log(tf.matrix_diag_part(L)))
    logNormalizingTerm = constantTerm + logDeterminantTerm
    return mahalanobisTerm + logNormalizingTerm * self.num_latent