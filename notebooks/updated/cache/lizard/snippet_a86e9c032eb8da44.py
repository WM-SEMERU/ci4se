def mergeReasons(self, others):
    reasons = []
    for req in ([self] + others):
        if req.reason and req.reason not in reasons:
            reasons.append(req.reason)
    return ', '.join(reasons)