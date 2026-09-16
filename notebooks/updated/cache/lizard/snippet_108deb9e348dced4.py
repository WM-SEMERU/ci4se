def VerifyMessageSignature(self, unused_response_comms, packed_message_list,
    cipher, cipher_verified, api_version, remote_public_key):
    _ = api_version
    result = rdf_flows.GrrMessage.AuthorizationState.UNAUTHENTICATED
    if cipher_verified or cipher.VerifyCipherSignature(remote_public_key):
        stats_collector_instance.Get().IncrementCounter(
            'grr_authenticated_messages')
        result = rdf_flows.GrrMessage.AuthorizationState.AUTHENTICATED
    if packed_message_list.timestamp != self.timestamp:
        result = rdf_flows.GrrMessage.AuthorizationState.UNAUTHENTICATED
    if not cipher.cipher_metadata:
        cipher.cipher_metadata = rdf_flows.CipherMetadata(source=
            packed_message_list.source)
    return result