def from_dict(cls, d):
    return cls(distance_cutoff=d['distance_cutoff'], angle_cutoff=d[
        'angle_cutoff'], additional_condition=d['additional_condition'],
        continuous_symmetry_measure_cutoff=d[
        'continuous_symmetry_measure_cutoff'], symmetry_measure_type=d[
        'symmetry_measure_type'])