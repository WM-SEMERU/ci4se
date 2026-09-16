def mtf_image_transformer_base_imagenet_mp64():
    hparams = mtf_image_transformer_base_imagenet()
    hparams.mesh_shape = 'model:8;batch:4'
    hparams.layout = 'batch:batch;d_ff:model;heads:model'
    hparams.batch_size = 8
    hparams.img_len = 64
    hparams.num_decoder_layers = 8
    return hparams