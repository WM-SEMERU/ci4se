def MultiAppend(self, value_timestamp_pairs):
    for value, timestamp in value_timestamp_pairs:
        self.Append(value, timestamp)