def cmu_mocap_49_balance(data_set='cmu_mocap'):
    train_motions = ['18', '19']
    test_motions = ['20']
    data = cmu_mocap('49', train_motions, test_motions, sample_every=4,
        data_set=data_set)
    data['info'] = (
        'One legged balancing motions from CMU data base subject 49. As used in Alvarez, Luengo and Lawrence at AISTATS 2009. It consists of '
         + data['info'])
    return data