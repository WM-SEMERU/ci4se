def build_payload(self, payload):
    for segment in self.segments:
        segment.pack(payload, commit=self.autocommit)