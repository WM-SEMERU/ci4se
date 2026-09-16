def get_gan_loss(self, true_frames, gen_frames, name):
    with tf.variable_scope('%s_discriminator' % name, reuse=tf.AUTO_REUSE):
        gan_d_loss, _, fake_logits_stop = self.d_step(true_frames, gen_frames)
    with tf.variable_scope('%s_discriminator' % name, reuse=True):
        gan_g_loss_pos_d, gan_g_loss_neg_d = self.g_step(gen_frames,
            fake_logits_stop)
    gan_g_loss = gan_g_loss_pos_d + gan_g_loss_neg_d
    tf.summary.scalar('gan_loss_%s' % name, gan_g_loss_pos_d + gan_d_loss)
    if self.hparams.gan_optimization == 'joint':
        gan_loss = gan_g_loss + gan_d_loss
    else:
        curr_step = self.get_iteration_num()
        gan_loss = tf.cond(tf.logical_not(curr_step % 2 == 0), lambda :
            gan_g_loss, lambda : gan_d_loss)
    return gan_loss