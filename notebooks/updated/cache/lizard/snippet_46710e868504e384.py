def register_token_network(self, token_registry_abi: Dict,
    token_registry_address: str, token_address: str,
    channel_participant_deposit_limit: Optional[int],
    token_network_deposit_limit: Optional[int]):
    with_limits = contracts_version_expects_deposit_limits(self.
        contracts_version)
    if with_limits:
        return self._register_token_network_with_limits(token_registry_abi,
            token_registry_address, token_address,
            channel_participant_deposit_limit, token_network_deposit_limit)
    else:
        return self._register_token_network_without_limits(token_registry_abi,
            token_registry_address, token_address,
            channel_participant_deposit_limit, token_network_deposit_limit)