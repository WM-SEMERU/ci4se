def get_common_session_key_proof_hash(self, session_key, session_key_proof,
    client_public):
    return self.hash(client_public, session_key_proof, session_key,
        as_bytes=True)