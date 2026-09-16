def __add_coreference_chain_tiers(self, docgraph, body, min_chain_length=3):
    E = self.E
    for i, chain in enumerate(get_pointing_chains(docgraph)):
        chain_tier = E('tier', {'id': 'TIE{}'.format(self.tier_count),
            'category': 'chain', 'type': 't', 'display-name':
            '[coref-chain-{}]'.format(i)})
        self.tier_count += 1
        chain_length = len(chain)
        if chain_length < min_chain_length:
            continue
        for j, node_id in enumerate(chain):
            span_node_ids = get_span(docgraph, node_id)
            if span_node_ids:
                start_id, end_id = self.__span2event(span_node_ids)
                element_str = 'chain_{0}: {1}/{2}'.format(i, chain_length -
                    j, chain_length)
                chain_tier.append(E('event', {'start': 'T{}'.format(
                    start_id), 'end': 'T{}'.format(end_id)}, element_str))
        body.append(chain_tier)