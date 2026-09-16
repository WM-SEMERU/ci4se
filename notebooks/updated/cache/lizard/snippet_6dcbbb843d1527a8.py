def ensure_all_alternatives_are_chosen(alt_id_col, choice_col, dataframe):
    all_ids = set(dataframe[alt_id_col].unique())
    chosen_ids = set(dataframe.loc[dataframe[choice_col] == 1, alt_id_col].
        unique())
    non_chosen_ids = all_ids.difference(chosen_ids)
    if len(non_chosen_ids) != 0:
        msg = (
            "The following alternative ID's were not chosen in any choice situation: \n{}"
            )
        raise ValueError(msg.format(non_chosen_ids))
    return None