def load_cufflinks_fpkm_dict(*args, **kwargs):
    return {row.id: row.fpkm for _, row in load_cufflinks_dataframe(*args,
        **kwargs).iterrows()}