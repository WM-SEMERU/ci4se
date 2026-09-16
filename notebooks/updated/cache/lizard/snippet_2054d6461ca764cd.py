def use_options(self, options, extractor=None):
    if not extractor:
        extracted = options
    else:
        extracted = extractor(self.template, options)
    if isinstance(extracted, dict):
        extracted = extracted.items()
    if extracted is not None:
        for key, val in extracted:
            self.values[self.normalise_key(key)] = val