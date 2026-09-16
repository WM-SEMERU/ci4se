def removeData(self, specfiles=None, rm=False, ci=False, smi=False, sai=
    False, si=False):
    if specfiles is None:
        specfiles = [_ for _ in viewkeys(self.info)]
    else:
        specfiles = aux.toList(specfiles)
    typeToContainer = {'rm': 'rmc', 'ci': 'cic', 'smi': 'smic', 'sai':
        'saic', 'si': 'sic'}
    datatypes = self._processDatatypes(rm, ci, smi, sai, si)
    for specfile in specfiles:
        for datatype in datatypes:
            datatypeContainer = typeToContainer[datatype]
            dataContainer = getattr(self, datatypeContainer)
            try:
                del dataContainer[specfile]
            except KeyError:
                pass
            finally:
                self.info[specfile]['status'][datatype] = False