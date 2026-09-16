def covariates_from_event_matrix(df, id_col):
    df = df.set_index(id_col)
    df = df.stack().reset_index()
    df.columns = [id_col, 'event', 'duration']
    df['_counter'] = 1
    return df.pivot_table(index=[id_col, 'duration'], columns='event',
        fill_value=0)['_counter'].reset_index()