def set_We(self, We, Eemin=None, Eemax=None, amplitude_name=None):
    We = validate_scalar('We', We, physical_type='energy')
    oldWe = self.compute_We(Eemin=Eemin, Eemax=Eemax)
    if amplitude_name is None:
        try:
            self.particle_distribution.amplitude *= (We / oldWe).decompose()
        except AttributeError:
            log.error(
                'The particle distribution does not have an attribute called amplitude to modify its normalization: you can set the name with the amplitude_name parameter of set_We'
                )
    else:
        oldampl = getattr(self.particle_distribution, amplitude_name)
        setattr(self.particle_distribution, amplitude_name, oldampl * (We /
            oldWe).decompose())