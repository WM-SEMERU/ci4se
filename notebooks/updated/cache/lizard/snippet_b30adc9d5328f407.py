def get_targets_bottom(modality_type, value=None):
    if modality_type == ModalityType.AUDIO:
        return make_targets_bottom(audio_bottom)
    elif modality_type == ModalityType.AUDIO_SPECTRAL:
        return make_targets_bottom(audio_spectral_bottom)
    elif modality_type in (ModalityType.CLASS_LABEL, ModalityType.
        MULTI_LABEL, ModalityType.ONE_HOT_CLASS_LABEL, ModalityType.
        SIGMOID_CLASS_LABEL, ModalityType.SIGMOID_MAX_POOLING_CLASS_LABEL,
        ModalityType.SOFTMAX_AVERAGE_POOLING_CLASS_LABEL, ModalityType.
        SOFTMAX_LAST_TIMESTEP_CLASS_LABEL, ModalityType.
        SOFTMAX_MAX_POOLING_CLASS_LABEL):
        return class_label_targets_bottom
    elif modality_type in (ModalityType.CTC_SYMBOL, ModalityType.SYMBOL,
        ModalityType.SYMBOL_WEIGHTS_ALL):
        return symbol_targets_bottom
    elif modality_type in (ModalityType.GENERIC_L2_LOSS, ModalityType.
        IDENTITY_SYMBOL):
        return identity_bottom
    elif modality_type == ModalityType.IDENTITY:
        return make_targets_bottom(identity_bottom)
    elif modality_type == ModalityType.IMAGE:
        return image_targets_bottom
    elif modality_type in (ModalityType.IMAGE_CHANNEL_BOTTOM_IDENTITY,
        ModalityType.IMAGE_CHANNEL_COMPRESS):
        return image_channel_compress_targets_bottom
    elif modality_type == ModalityType.IMAGE_CHANNEL_EMBEDDINGS_BOTTOM:
        return image_channel_embeddings_bottom
    elif modality_type in (ModalityType.REAL, ModalityType.REAL_L2_LOSS,
        ModalityType.REAL_LOG_POISSON_LOSS):
        return make_targets_bottom(real_bottom)
    elif modality_type == ModalityType.SPEECH_RECOGNITION:
        return make_targets_bottom(speech_recognition_bottom)
    elif modality_type == ModalityType.SYMBOL_ONE_HOT:
        return symbol_one_hot_bottom
    elif modality_type in (ModalityType.VIDEO, ModalityType.VIDEO_L1,
        ModalityType.VIDEO_L2):
        return video_targets_bottom
    elif modality_type == ModalityType.VIDEO_BITWISE:
        return video_bitwise_targets_bottom
    elif modality_type == ModalityType.VIDEO_IDENTITY:
        return video_identity_targets_bottom
    elif modality_type in (ModalityType.VIDEO_L1_RAW, ModalityType.VIDEO_L2_RAW
        ):
        return video_raw_targets_bottom
    elif modality_type == ModalityType.VIDEO_PIXEL_NOISE:
        return make_targets_bottom(video_pixel_noise_bottom)
    return value