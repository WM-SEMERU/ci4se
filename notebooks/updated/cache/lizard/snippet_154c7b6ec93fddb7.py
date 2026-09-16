def get_session_data(ctx, username, password, salt, server_public, private,
    preset):
    session = SRPClientSession(SRPContext(username, password, prime=preset[
        0], generator=preset[1]), private=private)
    session.process(server_public, salt, base64=True)
    click.secho('Client session key: %s' % session.key_b64)
    click.secho('Client session key proof: %s' % session.key_proof_b64)
    click.secho('Client session key hash: %s' % session.key_proof_hash_b64)