def dimod_object_hook(obj):
    if _is_sampleset_v2(obj):
        return SampleSet.from_serializable(obj)
    elif _is_bqm_v2(obj):
        return BinaryQuadraticModel.from_serializable(obj)
    return obj