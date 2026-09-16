def build_transgenic_lines(self):
    triples = []
    for cell_line in self.neuron_data:
        for tl in cell_line['donor']['transgenic_lines']:
            _id = tl['stock_number'] if tl['stock_number'] else tl['id']
            prefix = tl['transgenic_line_source_name']
            line_type = tl['transgenic_line_type_name']
            if prefix not in ['JAX', 'MMRRC', 'AIBS']:
                print(tc.red('WARNING:'), 'unknown prefix', prefix, json.
                    dumps(tl, indent=4))
                continue
            elif prefix == 'AIBS':
                prefix = 'AllenTL'
            _class = self.ns[prefix][str(_id)]
            triples.append((_class, rdf.type, owl.Class))
            triples.append((_class, rdfs.label, rdflib.Literal(tl['name'])))
            triples.append((_class, definition, rdflib.Literal(tl[
                'description'])))
            triples.append((_class, rdfs.subClassOf, ilxtr.transgenicLine))
            triples.append((_class, ilxtr.hasTransgenicType, ilxtr[
                line_type + 'Line']))
    transgenic_lines = simpleOnt(filename='allen-transgenic-lines', path=
        'ttl/generated/', prefixes=self.prefixes, triples=triples, comment=
        'Allen transgenic lines for cell types', branch=self.branch)
    transgenic_lines._graph.write()