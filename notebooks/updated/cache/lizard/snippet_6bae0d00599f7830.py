def const_shuffle(arr, seed=23980):
    old_seed = np.random.seed()
    np.random.seed(seed)
    np.random.shuffle(arr)
    np.random.seed(old_seed)