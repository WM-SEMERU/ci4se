def WriteSignedBinaryBlobs(binary_urn, blobs, token=None):
    if _ShouldUseLegacyDatastore():
        aff4.FACTORY.Delete(binary_urn, token=token)
        with data_store.DB.GetMutationPool() as mutation_pool:
            with aff4.FACTORY.Create(binary_urn, collects.GRRSignedBlob,
                mode='w', mutation_pool=mutation_pool, token=token) as fd:
                for blob in blobs:
                    fd.Add(blob, mutation_pool=mutation_pool)
    if data_store.RelationalDBEnabled():
        blob_references = rdf_objects.BlobReferences()
        current_offset = 0
        for blob in blobs:
            blob_id = data_store.BLOBS.WriteBlobWithUnknownHash(blob.
                SerializeToString())
            blob_references.items.Append(rdf_objects.BlobReference(offset=
                current_offset, size=len(blob.data), blob_id=blob_id))
            current_offset += len(blob.data)
        data_store.REL_DB.WriteSignedBinaryReferences(_SignedBinaryIDFromURN
            (binary_urn), blob_references)