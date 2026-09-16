def features(self, expand=False):
    fs = []
    if self._avm is not None:
        if len(self._feats) == len(self._avm):
            feats = self._feats
        else:
            feats = list(self._avm)
        for feat in feats:
            val = self._avm[feat]
            if isinstance(val, FeatureStructure):
                if not expand and val._is_notable():
                    fs.append((feat, val))
                else:
                    for subfeat, subval in val.features(expand=expand):
                        fs.append(('{}.{}'.format(feat, subfeat), subval))
            else:
                fs.append((feat, val))
    return fs