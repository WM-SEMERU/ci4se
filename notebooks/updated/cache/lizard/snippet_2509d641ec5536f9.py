def generate_evenly_distributed_data_sparse(dim=2000, num_active=40,
    num_samples=1000):
    indices = [numpy.random.choice(dim, size=num_active, replace=False) for
        _ in range(num_samples)]
    data = SM32()
    data.reshape(0, dim)
    for row in indices:
        data.addRowNZ(row, [1] * num_active)
    return data