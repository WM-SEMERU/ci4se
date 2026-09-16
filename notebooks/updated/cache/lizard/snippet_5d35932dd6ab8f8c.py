def serialize(graph: BELGraph, csv, sif, gsea, graphml, json, bel):
    if csv:
        log.info('Outputting CSV to %s', csv)
        to_csv(graph, csv)
    if sif:
        log.info('Outputting SIF to %s', sif)
        to_sif(graph, sif)
    if graphml:
        log.info('Outputting GraphML to %s', graphml)
        to_graphml(graph, graphml)
    if gsea:
        log.info('Outputting GRP to %s', gsea)
        to_gsea(graph, gsea)
    if json:
        log.info('Outputting JSON to %s', json)
        to_json_file(graph, json)
    if bel:
        log.info('Outputting BEL to %s', bel)
        to_bel(graph, bel)