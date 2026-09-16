def _ComputeUniquifier(self, debuggee):
    uniquifier = hashlib.sha1()
    if 'minorversion' not in debuggee.get('labels', []
        ) and 'sourceContexts' not in debuggee:
        uniquifier_computer.ComputeApplicationUniquifier(uniquifier)
    return uniquifier.hexdigest()