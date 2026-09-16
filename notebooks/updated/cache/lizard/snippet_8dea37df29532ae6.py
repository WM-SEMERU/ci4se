def can_pp_seq_no_be_in_view(self, view_no, pp_seq_no):
    if view_no > self.viewNo:
        raise PlenumValueError('view_no', view_no, '<= current view_no {}'.
            format(self.viewNo), prefix=self)
    return (view_no == self.viewNo or view_no < self.viewNo and self.
        last_prepared_before_view_change and compare_3PC_keys((view_no,
        pp_seq_no), self.last_prepared_before_view_change) >= 0)