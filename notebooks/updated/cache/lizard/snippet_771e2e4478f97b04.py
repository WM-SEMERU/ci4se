def tokens(self):
    for subsegment_or_token in self:
        if isinstance(subsegment_or_token, Segment):
            subsegment = subsegment_or_token
            for token in subsegment.tokens():
                yield token
        else:
            token = subsegment_or_token
            yield token