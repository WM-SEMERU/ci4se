def resolve(self, spec):
    address = Address.parse(spec)
    self.inject_address_closure(address)
    return self.transitive_subgraph_of_addresses([address])