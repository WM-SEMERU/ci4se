def write_source_description(self, capability_lists=None, outfile=None,
    links=None):
    rsd = SourceDescription(ln=links)
    rsd.pretty_xml = self.pretty_xml
    if capability_lists is not None:
        for uri in capability_lists:
            rsd.add_capability_list(uri)
    if outfile is None:
        print(rsd.as_xml())
    else:
        rsd.write(basename=outfile)