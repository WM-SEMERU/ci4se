def challenge_hash(peer_challenge, authenticator_challenge, username):
    sha_hash = hashlib.sha1()
    sha_hash.update(peer_challenge)
    sha_hash.update(authenticator_challenge)
    sha_hash.update(username)
    return sha_hash.digest()[:8]