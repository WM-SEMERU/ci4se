def _sign_block(self, block):
    block_header = block.block_header
    header_bytes = block_header.SerializeToString()
    signature = self._identity_signer.sign(header_bytes)
    block.set_signature(signature)
    return block