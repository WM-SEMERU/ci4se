def loginfo(method):

    def loginfo_method(self, rinput):
        klass = rinput.__class__
        for key in klass.stored():
            val = getattr(rinput, key)
            if isinstance(val, DataFrame):
                self.logger.debug('DataFrame %s', info.gather_info_dframe(val))
            elif isinstance(val, ObservationResult):
                for f in val.images:
                    self.logger.debug('OB DataFrame %s', info.
                        gather_info_dframe(f))
            else:
                pass
        result = method(self, rinput)
        return result
    return loginfo_method