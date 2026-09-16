def extract_features(self, data_frame, pre=''):
    try:
        return {(pre + 'frequency'): self.frequency(data_frame)[0], (pre +
            'mean_moving_time'): self.mean_moving_time(data_frame)[0], (pre +
            'incoordination_score'): self.incoordination_score(data_frame)[
            0], (pre + 'mean_alnt_target_distance'): self.
            mean_alnt_target_distance(data_frame)[0], (pre +
            'kinesia_scores'): self.kinesia_scores(data_frame)[0], (pre +
            'akinesia_times'): self.akinesia_times(data_frame)[0], (pre +
            'dysmetria_score'): self.dysmetria_score(data_frame)[0]}
    except:
        logging.error(
            'Error on FingerTappingProcessor process, extract features: %s',
            sys.exc_info()[0])