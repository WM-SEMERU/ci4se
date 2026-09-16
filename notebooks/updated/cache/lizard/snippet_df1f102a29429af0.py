def get_adjustments_for_sid(self, group, dates, requested_qtr_data,
    last_per_qtr, sid_to_idx, columns, col_to_all_adjustments,
    split_adjusted_asof_idx=None, split_adjusted_cols_for_group=None):
    all_adjustments_for_sid = {}
    sid = int(group.name)
    self.collect_overwrites_for_sid(group, dates, requested_qtr_data,
        last_per_qtr, sid_to_idx[sid], columns, all_adjustments_for_sid, sid)
    pre_adjustments, post_adjustments = (self.
        retrieve_split_adjustment_data_for_sid(dates, sid,
        split_adjusted_asof_idx))
    sid_estimates = self.estimates[self.estimates[SID_FIELD_NAME] == sid]
    for col_name in split_adjusted_cols_for_group:
        if col_name not in all_adjustments_for_sid:
            all_adjustments_for_sid[col_name] = {}
    self.collect_split_adjustments(all_adjustments_for_sid,
        requested_qtr_data, dates, sid, sid_to_idx[sid], sid_estimates,
        split_adjusted_asof_idx, pre_adjustments, post_adjustments,
        split_adjusted_cols_for_group)
    self.merge_into_adjustments_for_all_sids(all_adjustments_for_sid,
        col_to_all_adjustments)