def load_cufflinks_dict(*args, **kwargs):
    return {row.id: row for _, row in load_cufflinks_dataframe(*args, **
        kwargs).iterrows()}