def merge_recursive(obj_a, obj_b, level=False):
    return aggregate(obj_a, obj_b, level, map_class=AggregatedMap,
        sequence_class=AggregatedSequence)