def map_grounding(stmts_in, **kwargs):
    from indra.preassembler.grounding_mapper import GroundingMapper
    from indra.preassembler.grounding_mapper import gm as grounding_map
    from indra.preassembler.grounding_mapper import default_agent_map as agent_map
    logger.info('Mapping grounding on %d statements...' % len(stmts_in))
    do_rename = kwargs.get('do_rename')
    gm = kwargs.get('grounding_map', grounding_map)
    if do_rename is None:
        do_rename = True
    gm = GroundingMapper(gm, agent_map, use_deft=kwargs.get('use_deft', True))
    stmts_out = gm.map_agents(stmts_in, do_rename=do_rename)
    dump_pkl = kwargs.get('save')
    if dump_pkl:
        dump_statements(stmts_out, dump_pkl)
    return stmts_out