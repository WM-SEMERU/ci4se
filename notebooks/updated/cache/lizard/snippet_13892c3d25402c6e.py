def consecutive_frame(self):
    if self._frame.empty:
        return pd.DataFrame(columns=['pids', 'pl', 'cnt', 'is_win'])
    else:
        vals = (self._frame[PC.RET] >= 0).astype(int)
        seq = (vals.shift(1) != vals).astype(int).cumsum()

        def _do_apply(sub):
            return pd.Series({'pids': sub.index.values, 'pl': sub[PC.PL].
                sum(), 'cnt': len(sub.index), 'is_win': sub[PC.RET].iloc[0] >=
                0})
        return self._frame.groupby(seq).apply(_do_apply)