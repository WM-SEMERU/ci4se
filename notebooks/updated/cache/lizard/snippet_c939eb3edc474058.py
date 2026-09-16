def get_cond_latents_at_level(cond_latents, level, hparams):
    if cond_latents:
        if hparams.latent_dist_encoder in ['conv_net', 'conv3d_net']:
            return [cond_latent[level] for cond_latent in cond_latents]
        elif hparams.latent_dist_encoder in ['pointwise', 'conv_lstm']:
            return cond_latents[level]