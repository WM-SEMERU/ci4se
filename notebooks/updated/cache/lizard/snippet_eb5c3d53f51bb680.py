def Poisson(lamda, tag=None):
    assert lamda > 0, 'Poisson "lamda" must be greater than zero.'
    return uv(ss.poisson(lamda), tag=tag)