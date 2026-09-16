def hparams(self, defaults, unused_model_hparams):
    super(BabiQa, self).hparams(defaults, unused_model_hparams)
    p = defaults
    num_classes = self._encoders['targets'].vocab_size
    p.modality = {'targets': modalities.ModalityType.CLASS_LABEL}
    p.vocab_size = {'targets': num_classes}