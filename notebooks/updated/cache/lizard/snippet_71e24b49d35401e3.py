def _create_trial_info(self, expr_dir):
    meta = self._build_trial_meta(expr_dir)
    self.logger.debug('Create trial for %s' % meta)
    trial_record = TrialRecord.from_json(meta)
    trial_record.save()