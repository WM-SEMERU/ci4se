def qmed(self, method='best', **method_options):
    if method == 'best':
        if self.catchment.pot_dataset:
            if self.catchment.amax_records:
                if (self.catchment.record_length <= self.catchment.
                    pot_dataset.record_length < 14):
                    use_method = 'pot_records'
                elif self.catchment.record_length >= 2:
                    use_method = 'amax_records'
                else:
                    use_method = None
            elif self.catchment.pot_dataset.record_length >= 1:
                use_method = 'pot_records'
            else:
                use_method = None
        elif self.catchment.record_length >= 2:
            use_method = 'amax_records'
        else:
            use_method = None
        if use_method:
            self.results_log['method'] = use_method
            return getattr(self, '_qmed_from_' + use_method)()
        for method in self.methods[1:]:
            try:
                self.results_log['method'] = method
                return getattr(self, '_qmed_from_' + method)(**method_options)
            except (TypeError, InsufficientDataError):
                pass
        return None
    else:
        try:
            self.results_log['method'] = method
            return getattr(self, '_qmed_from_' + method)(**method_options)
        except AttributeError:
            raise AttributeError('Method `{}` to estimate QMED does not exist.'
                .format(method))