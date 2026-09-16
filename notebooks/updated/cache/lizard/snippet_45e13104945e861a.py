def check_availability(self, isos):
    iso1name = iso_name_converter(isos[0])
    iso2name = iso_name_converter(isos[1])
    ratio = iso1name + '/' + iso2name
    ratio_inv = iso2name + '/' + iso1name
    delta = 'd(' + iso1name + '/' + iso2name + ')'
    delta_inv = 'd(' + iso2name + '/' + iso1name + ')'
    index = -1
    try:
        index = self.datadict[ratio]
        delta_b = False
        ratio_b = False
    except KeyError:
        try:
            index = self.datadict[ratio_inv]
            delta_b = False
            ratio_b = True
        except KeyError:
            try:
                index = self.datadict[delta]
                delta_b = True
                ratio_b = False
            except KeyError:
                try:
                    index = self.datadict[delta_inv]
                    delta_b = True
                    ratio_b = True
                except KeyError:
                    index = -1
                    delta_b = None
                    ratio_b = None
    return index, delta_b, ratio_b