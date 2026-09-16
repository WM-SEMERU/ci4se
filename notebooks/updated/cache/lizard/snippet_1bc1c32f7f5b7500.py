def run_action(self, feature, action, run_if_error=False, raise_exception=True
    ):
    if len(self._error_dict[feature]) > 0 and not run_if_error:
        return
    error = None
    instance = self.features[feature]
    try:
        getattr(instance, action)()
    except Exception as e:
        e = sys.exc_info()[1]
        self.logger.info(
            'An exception occurred with action %s in feature %s!' % (action,
            feature))
        self.logger.debug('Exception', exc_info=sys.exc_info())
        error = str(e)
        self.log_feature_error(feature, str(e))
    if error is not None and raise_exception:
        exception_msg = '%s action failed for feature %s: %s' % (action,
            feature, error)
        if self.phase == PHASE.REMOVE:
            raise FormulaException(exception_msg)
        else:
            raise SprinterException(exception_msg)
    return error