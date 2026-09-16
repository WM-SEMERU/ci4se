def mutate(self, info_in):
    if self.failed:
        raise ValueError('{} cannot mutate as it has failed.'.format(self))
    from transformations import Mutation
    info_out = type(info_in)(origin=self, contents=info_in._mutated_contents())
    Mutation(info_in=info_in, info_out=info_out)