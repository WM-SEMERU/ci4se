def _read_optimized_geometry(self):
    header_pattern = (
        '\\*+\\s+OPTIMIZATION\\s+CONVERGED\\s+\\*+\\s+\\*+\\s+Coordinates \\(Angstroms\\)\\s+ATOM\\s+X\\s+Y\\s+Z'
        )
    table_pattern = (
        '\\s+\\d+\\s+\\w+\\s+([\\d\\-\\.]+)\\s+([\\d\\-\\.]+)\\s+([\\d\\-\\.]+)'
        )
    footer_pattern = '\\s+Z-matrix Print:'
    parsed_optimized_geometry = read_table_pattern(self.text,
        header_pattern, table_pattern, footer_pattern)
    if parsed_optimized_geometry == [] or None:
        self.data['optimized_geometry'] = None
        header_pattern = (
            '^\\s+\\*+\\s+OPTIMIZATION CONVERGED\\s+\\*+\\s+\\*+\\s+Z-matrix\\s+Print:\\s+\\$molecule\\s+[\\d\\-]+\\s+[\\d\\-]+\\n'
            )
        table_pattern = (
            '\\s*(\\w+)(?:\\s+(\\d+)\\s+([\\d\\-\\.]+)(?:\\s+(\\d+)\\s+([\\d\\-\\.]+)(?:\\s+(\\d+)\\s+([\\d\\-\\.]+))*)*)*(?:\\s+0)*'
            )
        footer_pattern = '^\\$end\\n'
        self.data['optimized_zmat'] = read_table_pattern(self.text,
            header_pattern, table_pattern, footer_pattern)
    else:
        self.data['optimized_geometry'] = process_parsed_coords(
            parsed_optimized_geometry[0])
        if self.data.get('charge') != None:
            self.data['molecule_from_optimized_geometry'] = Molecule(species
                =self.data.get('species'), coords=self.data.get(
                'optimized_geometry'), charge=self.data.get('charge'),
                spin_multiplicity=self.data.get('multiplicity'))