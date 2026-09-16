def from_sequence(cls, sequence, phos_3_prime=False):
    strand1 = NucleicAcidStrand(sequence, phos_3_prime=phos_3_prime)
    duplex = cls(strand1)
    return duplex