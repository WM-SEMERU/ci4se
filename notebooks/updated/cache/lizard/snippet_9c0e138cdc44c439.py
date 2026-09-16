def _check_challenge(cls, challenge, challenge_body):
    if challenge.uri != challenge_body.uri:
        raise errors.UnexpectedUpdate(challenge.uri)
    return challenge