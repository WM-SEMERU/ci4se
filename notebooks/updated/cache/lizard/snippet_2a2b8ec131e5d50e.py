def get_variation(self, experiment, user_id, attributes,
    ignore_user_profile=False):
    if not experiment_helper.is_experiment_running(experiment):
        self.logger.info('Experiment "%s" is not running.' % experiment.key)
        return None
    variation = self.config.get_forced_variation(experiment.key, user_id)
    if variation:
        return variation
    variation = self.get_forced_variation(experiment, user_id)
    if variation:
        return variation
    user_profile = UserProfile(user_id)
    if not ignore_user_profile and self.user_profile_service:
        try:
            retrieved_profile = self.user_profile_service.lookup(user_id)
        except:
            self.logger.exception(
                'Unable to retrieve user profile for user "%s" as lookup failed.'
                 % user_id)
            retrieved_profile = None
        if validator.is_user_profile_valid(retrieved_profile):
            user_profile = UserProfile(**retrieved_profile)
            variation = self.get_stored_variation(experiment, user_profile)
            if variation:
                return variation
        else:
            self.logger.warning('User profile has invalid format.')
    if not audience_helper.is_user_in_experiment(self.config, experiment,
        attributes, self.logger):
        self.logger.info(
            'User "%s" does not meet conditions to be in experiment "%s".' %
            (user_id, experiment.key))
        return None
    bucketing_id = self._get_bucketing_id(user_id, attributes)
    variation = self.bucketer.bucket(experiment, user_id, bucketing_id)
    if variation:
        if not ignore_user_profile and self.user_profile_service:
            try:
                user_profile.save_variation_for_experiment(experiment.id,
                    variation.id)
                self.user_profile_service.save(user_profile.__dict__)
            except:
                self.logger.exception(
                    'Unable to save user profile for user "%s".' % user_id)
        return variation
    return None