def build_tri(adf):
    cap, inc = adf.columns[1:3]
    data = adf[[cap, inc]]
    inc_pct = data[inc].div(data[cap].shift(1))
    cap_pct = data[cap].pct_change(1)
    pre_final = inc_pct + cap_pct
    final_df = pd.concat([adf.override_feed000, pre_final, adf.
        failsafe_feed999], axis=1)
    final_df = final_df.apply(_row_wise_priority, axis=1)
    return final_df