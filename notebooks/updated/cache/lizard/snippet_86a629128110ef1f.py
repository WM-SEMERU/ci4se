def proc_state(self, state_data, state_id):
    assembly = Assembly(assembly_id=state_id)
    for k, chain in sorted(state_data.items()):
        assembly._molecules.append(self.proc_chain(chain, assembly))
    return assembly