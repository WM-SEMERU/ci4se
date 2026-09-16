def next_frame_ae_tiny():
    hparams = next_frame_tiny()
    hparams.bottom['inputs'] = modalities.video_bitwise_bottom
    hparams.top['inputs'] = modalities.video_top
    hparams.batch_size = 8
    hparams.dropout = 0.4
    return hparams