def _handle_calls(self, alts, format_, format_str, arr):
    if format_str not in self._format_cache:
        self._format_cache[format_str] = list(map(self.header.
            get_format_field_info, format_))
    calls = []
    for sample, raw_data in zip(self.samples.names, arr[9:]):
        if self.samples.is_parsed(sample):
            data = self._parse_calls_data(format_, self._format_cache[
                format_str], raw_data)
            call = record.Call(sample, data)
            self._format_checker.run(call, len(alts))
            self._check_filters(call.data.get('FT'), 'FORMAT/FT', call.sample)
            calls.append(call)
        else:
            calls.append(record.UnparsedCall(sample, raw_data))
    return calls