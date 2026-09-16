def create(backbone: ModelFactory, input_block: typing.Optional[
    ModelFactory]=None, initial_std_dev=0.4, factorized_noise=True):
    if input_block is None:
        input_block = IdentityFactory()
    return NoisyQModelFactory(input_block=input_block, backbone=backbone,
        initial_std_dev=initial_std_dev, factorized_noise=factorized_noise)