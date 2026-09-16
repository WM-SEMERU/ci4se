def _strip_stray_atoms(self):
    components = self.bond_graph.connected_components()
    major_component = max(components, key=len)
    for atom in list(self.particles()):
        if atom not in major_component:
            self.remove(atom)