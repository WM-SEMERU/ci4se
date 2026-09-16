def as_df(self, ignore_vals=['history'], separator='.', verbose=True):

    def add_eval(res):
        if 'eval' not in res:
            if isinstance(res['history'], list):
                eval_names = list(res['history'][0]['loss'].keys())
                eval_metrics = np.array([[v[-1] for k, v in hist['loss'].
                    items()] for hist in res['history']]).mean(axis=0).tolist()
                res['eval'] = {eval_names[i]: eval_metrics[i] for i in
                    range(len(eval_metrics))}
            else:
                res['eval'] = {k: v[-1] for k, v in res['history']['loss'].
                    items()}
        return res

    def add_n_epoch(df):
        df_epoch = self.train_history().groupby('tid')['epoch'].max(
            ).reset_index()
        df_epoch.rename(columns={'epoch': 'n_epoch'}, inplace=True)
        return pd.merge(df, df_epoch, on='tid', how='left')
    results = self.get_ok_results(verbose=verbose)
    rp = [_flatten_dict(_delete_keys(add_eval(x), ignore_vals), separator) for
        x in results]
    df = pd.DataFrame.from_records(rp)
    df = add_n_epoch(df)
    first = ['tid', 'loss', 'status']
    return _put_first(df, first)