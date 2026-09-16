def _generate_mix2pl_dataset(n, m, outfile, useDirichlet=True):
    params, votes = generate_mix2pl_dataset(n, m, useDirichlet)
    outfile.write(str(m) + ',' + str(n) + '\n')
    outfile.write(','.join(map(str, params)) + '\n')
    for vote in votes:
        outfile.write(','.join(map(str, vote)) + '\n')
    return params, votes