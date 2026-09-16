def gen_experiment_id(n=10):
    chrs = 'abcdefghijklmnopqrstuvwxyz'
    inds = np.random.randint(0, len(chrs), size=n)
    return ''.join([chrs[i] for i in inds])