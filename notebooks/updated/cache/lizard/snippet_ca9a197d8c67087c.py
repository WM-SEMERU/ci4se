def use_bcbio_variation_recall(algs):
    for alg in algs:
        jointcaller = alg.get('jointcaller', [])
        if not isinstance(jointcaller, (tuple, list)):
            jointcaller = [jointcaller]
        for caller in jointcaller:
            if caller not in set(['gatk-haplotype-joint', None, False]):
                return True
    return False