def make_ring_filename(self, source_name, ring, galprop_run):
    format_dict = self.__dict__.copy()
    format_dict['sourcekey'] = self._name_factory.galprop_ringkey(source_name
        =source_name, ringkey='ring_%i' % ring)
    format_dict['galprop_run'] = galprop_run
    return self._name_factory.galprop_gasmap(**format_dict)