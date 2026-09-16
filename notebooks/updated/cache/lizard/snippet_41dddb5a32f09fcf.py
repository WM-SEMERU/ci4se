def Handle(self, args, token=None):
    artifacts_list = sorted(artifact_registry.REGISTRY.GetArtifacts(
        reload_datastore_artifacts=True), key=lambda art: art.name)
    total_count = len(artifacts_list)
    if args.count:
        artifacts_list = artifacts_list[args.offset:args.offset + args.count]
    else:
        artifacts_list = artifacts_list[args.offset:]
    descriptors = self.BuildArtifactDescriptors(artifacts_list)
    return ApiListArtifactsResult(items=descriptors, total_count=total_count)