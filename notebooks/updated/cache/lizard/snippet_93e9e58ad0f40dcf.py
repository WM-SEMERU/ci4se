def output_files(self):
    for dep in self.subgraph.successors(self.address):
        dep_rule = self.subgraph.node[dep]['target_obj']
        for out_file in dep_rule.output_files:
            yield out_file