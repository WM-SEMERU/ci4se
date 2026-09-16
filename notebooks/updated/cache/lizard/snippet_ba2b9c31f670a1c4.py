def _normalize_data_types(self, strategy):
    for k, v in strategy.iteritems():
        if not isinstance(v, str):
            continue
        if v == 'true':
            strategy[k] = True
        elif v == 'false' or v is None:
            strategy[k] = False
        else:
            try:
                if v.find('.') > 0:
                    strategy[k] = float(v)
                else:
                    strategy[k] = int(v)
            except ValueError:
                pass