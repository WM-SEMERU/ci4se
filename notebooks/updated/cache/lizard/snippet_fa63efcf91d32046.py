def get_report(self):
    lines = [super(LabelCoverageValidationResult, self).get_report()]
    if len(self.uncovered_segments) > 0:
        lines.append('\nUncovered segments:')
        for utt_idx, utt_segments in self.uncovered_segments.items():
            if len(utt_segments) > 0:
                lines.append('\n{}'.format(utt_idx))
                sorted_items = sorted(utt_segments, key=lambda x: x[0])
                lines.extend(['    * {:10.2f}  -  {:10.2f}'.format(x[0], x[
                    1]) for x in sorted_items])
    return '\n'.join(lines)