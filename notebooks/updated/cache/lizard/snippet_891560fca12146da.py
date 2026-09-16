def to_text_format(self):
    return '\n'.join(itertools.chain((self.fetch_date.strftime(
        '%Y%m%d%H%M%S'),), (rr.to_text() for rr in self.resource_records), ()))