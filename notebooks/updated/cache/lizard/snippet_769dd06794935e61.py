def _is_inside(self, span1, span2, covered_spans):
    if self._is_span_inside(span1, covered_spans[0]) and self._is_span_inside(
        span2, covered_spans[1]):
        return True
    return False