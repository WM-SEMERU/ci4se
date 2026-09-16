def _process_stocks(self, limit):
    if self.test_mode:
        graph = self.testgraph
    else:
        graph = self.graph
    model = Model(graph)
    line_counter = 0
    raw = '/'.join((self.rawdir, 'stock'))
    LOG.info('building labels for stocks')
    with open(raw, 'r') as f:
        f.readline()
        filereader = csv.reader(f, delimiter='\t', quotechar='"')
        for line in filereader:
            line_counter += 1
            (stock_id, dbxref_id, organism_id, name, uniquename,
                description, type_id, is_obsolete) = line
            stock_num = stock_id
            stock_id = 'FlyBase:' + uniquename
            self.idhash['stock'][stock_num] = stock_id
            stock_label = description
            organism_key = organism_id
            taxon = self.idhash['organism'][organism_key]
            if (not self.test_mode and limit is not None and line_counter >
                limit):
                pass
            else:
                if self.test_mode and int(stock_num) not in self.test_keys[
                    'strain']:
                    continue
                model.addClassToGraph(taxon)
                model.addIndividualToGraph(stock_id, stock_label, taxon)
                if is_obsolete == 't':
                    model.addDeprecatedIndividual(stock_id)
    return