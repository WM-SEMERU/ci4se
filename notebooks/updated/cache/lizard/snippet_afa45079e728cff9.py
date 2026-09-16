def poll_until_valid(authzr, clock, client, timeout=300.0):

    def repoll(result):
        authzr, retry_after = result
        if authzr.body.status in {STATUS_PENDING, STATUS_PROCESSING}:
            return deferLater(clock, retry_after, lambda : None).addCallback(
                lambda _: client.poll(authzr)).addCallback(repoll)
        if authzr.body.status != STATUS_VALID:
            raise AuthorizationFailed(authzr)
        return authzr

    def cancel_timeout(result):
        if timeout_call.active():
            timeout_call.cancel()
        return result
    d = client.poll(authzr).addCallback(repoll)
    timeout_call = clock.callLater(timeout, d.cancel)
    d.addBoth(cancel_timeout)
    return d