def nt(graph):
    from rdflib import ConjunctiveGraph
    from rdflib.plugin import register, Parser
    register('json-ld', Parser, 'rdflib_jsonld.parser', 'JsonLDParser')
    click.echo(ConjunctiveGraph().parse(data=_jsonld(graph, 'expand'),
        format='json-ld').serialize(format='nt'))