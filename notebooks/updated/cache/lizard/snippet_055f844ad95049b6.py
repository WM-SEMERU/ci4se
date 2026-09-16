def get_ntp_stats(self):
    ntp_stats = []
    REGEX = (
        '^\\s?(\\+|\\*|x|-)?([a-zA-Z0-9\\.+-:]+)\\s+([a-zA-Z0-9\\.]+)\\s+([0-9]{1,2})\\s+(-|u)\\s+([0-9h-]+)\\s+([0-9]+)\\s+([0-9]+)\\s+([0-9\\.]+)\\s+([0-9\\.-]+)\\s+([0-9\\.]+)\\s?$'
        )
    ntp_assoc_output = self.device.cli('show ntp associations no-resolve')
    ntp_assoc_output_lines = ntp_assoc_output.splitlines()
    for ntp_assoc_output_line in ntp_assoc_output_lines[3:]:
        line_search = re.search(REGEX, ntp_assoc_output_line, re.I)
        if not line_search:
            continue
        line_groups = line_search.groups()
        try:
            ntp_stats.append({'remote': napalm.base.helpers.ip(line_groups[
                1]), 'synchronized': line_groups[0] == '*', 'referenceid':
                py23_compat.text_type(line_groups[2]), 'stratum': int(
                line_groups[3]), 'type': py23_compat.text_type(line_groups[
                4]), 'when': py23_compat.text_type(line_groups[5]),
                'hostpoll': int(line_groups[6]), 'reachability': int(
                line_groups[7]), 'delay': float(line_groups[8]), 'offset':
                float(line_groups[9]), 'jitter': float(line_groups[10])})
        except Exception:
            continue
    return ntp_stats