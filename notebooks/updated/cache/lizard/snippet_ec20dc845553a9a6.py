def train_history(self, tid=None):

    def result2history(result):
        if isinstance(result['history'], list):
            return pd.concat([pd.DataFrame(hist['loss']).assign(fold=i) for
                i, hist in enumerate(result['history'])])
        else:
            return pd.DataFrame(result['history']['loss'])
    if tid is None:
        tid = self.valid_tid()
    res = [result2history(t['result']).assign(tid=t['tid']) for t in self.
        trials if t['tid'] in _listify(tid)]
    df = pd.concat(res)
    fold_name = ['fold'] if 'fold' in df else []
    df = _put_first(df, ['tid'] + fold_name + ['epoch'])
    return df