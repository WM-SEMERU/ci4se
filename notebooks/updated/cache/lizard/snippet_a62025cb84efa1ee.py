def _calc_dic(self):
    mean_deviance = np.mean(self.db.trace('deviance')(), axis=0)
    for stochastic in self.stochastics:
        try:
            mean_value = np.mean(self.db.trace(stochastic.__name__)(), axis=0)
            stochastic.value = mean_value
        except KeyError:
            print_('No trace available for %s. DIC value may not be valid.' %
                stochastic.__name__)
        except TypeError:
            print_('Not able to calculate DIC: invalid stochastic %s' %
                stochastic.__name__)
            return None
    return 2 * mean_deviance - self.deviance