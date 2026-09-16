def decode(self, dataset_split=None, decode_from_file=False,
    checkpoint_path=None):
    if decode_from_file:
        decoding.decode_from_file(self._estimator, self._decode_hparams.
            decode_from_file, self._hparams, self._decode_hparams, self.
            _decode_hparams.decode_to_file)
    else:
        decoding.decode_from_dataset(self._estimator, self._hparams.problem
            .name, self._hparams, self._decode_hparams, dataset_split=
            dataset_split, checkpoint_path=checkpoint_path)