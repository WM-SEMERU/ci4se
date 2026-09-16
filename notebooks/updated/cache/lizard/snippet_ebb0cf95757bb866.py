def _merge_tops_merge(self, tops):
    top = DefaultOrderedDict(OrderedDict)
    base_tops = tops.pop('base', DefaultOrderedDict(OrderedDict))
    for ctop in base_tops:
        for saltenv, targets in six.iteritems(ctop):
            if saltenv == 'include':
                continue
            try:
                for tgt in targets:
                    top[saltenv][tgt] = ctop[saltenv][tgt]
            except TypeError:
                raise SaltRenderError(
                    'Unable to render top file. No targets found.')
    for cenv, ctops in six.iteritems(tops):
        for ctop in ctops:
            for saltenv, targets in six.iteritems(ctop):
                if saltenv == 'include':
                    continue
                elif saltenv != cenv:
                    log.debug(
                        "Section for saltenv '%s' in the '%s' saltenv's top file will be ignored, as the top_file_merging_strategy is set to 'merge' and the saltenvs do not match"
                        , saltenv, cenv)
                    continue
                elif saltenv in top:
                    log.debug(
                        "Section for saltenv '%s' in the '%s' saltenv's top file will be ignored, as this saltenv was already defined in the 'base' top file"
                        , saltenv, cenv)
                    continue
                try:
                    for tgt in targets:
                        top[saltenv][tgt] = ctop[saltenv][tgt]
                except TypeError:
                    raise SaltRenderError(
                        'Unable to render top file. No targets found.')
    return top