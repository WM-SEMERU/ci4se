def get_band_gap(self):
    dosdata = self.get_dos()
    if type(dosdata) == type(None):
        return None
    else:
        energy = dosdata.conditions.scalars
        dos = dosdata.scalars
        step_size = energy[1].value - energy[0].value
        not_found = True
        l = 0
        bot = 10 ** 3
        top = -10 ** 3
        while not_found and l < len(dos):
            e = float(energy[l].value)
            dens = float(dos[l].value)
            if e < 0 and dens > 0.001:
                bot = e
            elif e > 0 and dens > 0.001:
                top = e
                not_found = False
            l += 1
        if top < bot:
            raise Exception('Algorithm failed to find the band gap')
        elif top - bot < step_size * 2:
            return Property(scalars=[Scalar(value=0)], units='eV')
        else:
            bandgap = float(top - bot)
            return Property(scalars=[Scalar(value=round(bandgap, 3))],
                units='eV')