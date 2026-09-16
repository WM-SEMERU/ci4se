def printBasicInfo(onto):
    rdfGraph = onto.rdfGraph
    print('_' * 50, '\n')
    print('TRIPLES = %s' % len(rdfGraph))
    print('_' * 50)
    print('\nNAMESPACES:\n')
    for x in onto.ontologyNamespaces:
        print('%s : %s' % (x[0], x[1]))
    print('_' * 50, '\n')
    print('ONTOLOGY METADATA:\n')
    for x, y in onto.ontologyAnnotations():
        print('%s: \n\t %s' % (uri2niceString(x, onto.ontologyNamespaces),
            uri2niceString(y, onto.ontologyNamespaces)))
    print('_' * 50, '\n')
    print('CLASS TAXONOMY:\n')
    onto.printClassTree()
    print('_' * 50, '\n')