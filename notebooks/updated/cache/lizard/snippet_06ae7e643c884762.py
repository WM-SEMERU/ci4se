def irfs(self, **kwargs):
    dsval = kwargs.get('dataset', self.dataset(**kwargs))
    tokens = dsval.split('_')
    irf_name = '%s_%s_%s' % (DATASET_DICTIONARY['%s_%s' % (tokens[0],
        tokens[1])], EVCLASS_NAME_DICTIONARY[tokens[3]], kwargs.get('irf_ver'))
    return irf_name