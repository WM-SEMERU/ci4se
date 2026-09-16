def publish_proto_metadata_update(self):
    metadata = load_mpe_service_metadata(self.args.metadata_file)
    ipfs_hash_base58 = utils_ipfs.publish_proto_in_ipfs(self.
        _get_ipfs_client(), self.args.protodir)
    metadata.set_simple_field('model_ipfs_hash', ipfs_hash_base58)
    metadata.save_pretty(self.args.metadata_file)