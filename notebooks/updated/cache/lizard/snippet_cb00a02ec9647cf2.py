def _transcript_feature_positions(self, feature):
    ranges = self._transcript_feature_position_ranges(feature, required=True)
    results = []
    for start, end in ranges:
        for position in range(start, end + 1):
            assert position not in results, 'Repeated position %d for %s' % (
                position, feature)
            results.append(position)
    return results