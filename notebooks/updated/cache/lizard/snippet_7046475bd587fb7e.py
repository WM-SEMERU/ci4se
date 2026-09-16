def getFullBeamline(self, beamlineKw, extend=False):
    try:
        assert beamlineKw.upper() in self.kws_bl
        rawbl = self.getBeamline(beamlineKw)
        fullbl = []
        if not extend:
            for ele in rawbl:
                if self.isBeamline(ele):
                    fullbl.extend(self.getFullBeamline(ele))
                else:
                    fullbl.append(ele)
        else:
            for ele in rawbl:
                ele_num_name_dict = self.rinseElement(ele)
                elename = ele_num_name_dict['name']
                elenum = ele_num_name_dict['num']
                if self.isBeamline(elename):
                    fullbl.extend(self.getFullBeamline(elename, extend=True
                        ) * elenum)
                else:
                    fullbl.extend([elename] * elenum)
        return fullbl
    except AssertionError:
        print('ERROR: %s is not a right defined beamline.' % beamlineKw)