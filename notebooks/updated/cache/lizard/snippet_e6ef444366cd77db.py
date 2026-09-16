def narrow_sqs(self, sqs):
    if self.select_many:
        sq = None
        for value in self.get_applicable_values():
            q = SQ(**{self.field_name: sqs.query.clean(value.value)})
            if sq:
                sq = sq | q
            else:
                sq = q
        if sq:
            sqs = sqs.narrow(sq)
    else:
        for value in self.get_applicable_values():
            sqs = sqs.narrow('%s:"%s"' % (self.field_name, sqs.query.clean(
                value.value)))
    return sqs