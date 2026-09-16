def get_report(self):
    lines = [super(InvalidUtterancesResult, self).get_report()]
    if len(self.invalid_utterances) > 0:
        lines.append('\nInvalid utterances:')
        sorted_items = sorted(self.invalid_utterances.items(), key=lambda x:
            x[0])
        lines.extend(['    * {} ({})'.format(x, y) for x, y in sorted_items])
    return '\n'.join(lines)