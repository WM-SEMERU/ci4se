def configure(self, options, conf):
    super(Nosebook, self).configure(options, conf)
    self.testMatch = re.compile(options.nosebookTestMatch).match
    self.testMatchCell = re.compile(options.nosebookTestMatchCell).match
    scrubs = []
    if options.nosebookScrub:
        try:
            scrubs = json.loads(options.nosebookScrub)
        except Exception:
            scrubs = [options.nosebookScrub]
    if isstr(scrubs):
        scrubs = {scrubs: '<...>'}
    elif not isinstance(scrubs, dict):
        scrubs = dict([(scrub, '<...%s>' % i) for i, scrub in enumerate(
            scrubs)])
    self.scrubMatch = {re.compile(scrub): sub for scrub, sub in scrubs.items()}