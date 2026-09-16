def denoise_v1_m15():
    hparams = xmoe2_v1()
    hparams.decoder_layers = [('att' if l == 'local_att' else l) for l in
        hparams.decoder_layers]
    hparams.decoder_type = 'denoising'
    hparams.noising_spec_train = {'type': 'mask', 'prob': 0.15}
    return hparams