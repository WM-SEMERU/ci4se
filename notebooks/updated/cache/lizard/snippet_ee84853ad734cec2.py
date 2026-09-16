def windows_df(self):
    import pandas as pd
    if self.windows is None:
        raise Exception('You need to call the block_windows or windows before.'
            )
    df_wins = []
    for row, col, win in zip(self.windows_row, self.windows_col, self.windows):
        df_wins.append(pd.DataFrame({'row': [row], 'col': [col], 'Window':
            [win]}))
    df_wins = pd.concat(df_wins).set_index(['row', 'col'])
    df_wins['window_index'] = range(df_wins.shape[0])
    df_wins = df_wins.sort_index()
    return df_wins