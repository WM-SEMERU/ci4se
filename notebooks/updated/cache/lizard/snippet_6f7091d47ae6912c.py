def _get_text_for_grounding(stmt, agent_text):
    text = None
    try:
        from indra_db.util.content_scripts import get_text_content_from_text_refs
        from indra.literature.deft_tools import universal_extract_text
        refs = stmt.evidence[0].text_refs
        if stmt.evidence[0].pmid:
            refs['PMID'] = stmt.evidence[0].pmid
        logger.info('Obtaining text for disambiguation with refs: %s' % refs)
        content = get_text_content_from_text_refs(refs)
        text = universal_extract_text(content, contains=agent_text)
        if text:
            return text
    except Exception as e:
        logger.info('Could not get text for disambiguation from DB.')
    if text is None:
        from indra.literature import pubmed_client
        pmid = stmt.evidence[0].pmid
        if pmid:
            logger.info('Obtaining abstract for disambiguation for PMID%s' %
                pmid)
            text = pubmed_client.get_abstract(pmid)
            if text:
                return text
    if text is None:
        logger.info('Falling back on sentence-based disambiguation')
        text = stmt.evidence[0].text
        return text
    return None