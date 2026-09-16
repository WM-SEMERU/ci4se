def recompute_missing_neighbors(self):
    oon_records = [r for r in self.records if self.network.get(r.
        correspondent_id, None) is None]
    num_oon_calls = len([r for r in oon_records if r.interaction == 'call'])
    num_oon_texts = len([r for r in oon_records if r.interaction == 'text'])
    num_oon_neighbors = len(set(x.correspondent_id for x in oon_records))
    oon_call_durations = sum([r.call_duration for r in oon_records if r.
        interaction == 'call'])
    num_calls = len([r for r in self.records if r.interaction == 'call'])
    num_texts = len([r for r in self.records if r.interaction == 'text'])
    total_neighbors = len(set(x.correspondent_id for x in self.records))
    total_call_durations = sum([r.call_duration for r in self.records if r.
        interaction == 'call'])

    def _safe_div(a, b, default):
        return a / b if b != 0 else default
    self.percent_outofnetwork_calls = _safe_div(num_oon_calls, num_calls, 0)
    self.percent_outofnetwork_texts = _safe_div(num_oon_texts, num_texts, 0)
    self.percent_outofnetwork_contacts = _safe_div(num_oon_neighbors,
        total_neighbors, 0)
    self.percent_outofnetwork_call_durations = _safe_div(oon_call_durations,
        total_call_durations, 0)