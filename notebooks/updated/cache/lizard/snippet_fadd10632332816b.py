def qrandom(n):
    import quantumrandom
    return np.concatenate([quantumrandom.get_data(data_type='uint16',
        array_length=1024) for i in range(int(np.ceil(n / 1024.0)))])[:n]