def from_specification(cls, specification, model, classical_gap, ground_energy
    ):
    return cls(specification.graph, specification.decision_variables,
        specification.feasible_configurations, specification.vartype, model,
        classical_gap, ground_energy, ising_linear_ranges=specification.
        ising_linear_ranges, ising_quadratic_ranges=specification.
        ising_quadratic_ranges)