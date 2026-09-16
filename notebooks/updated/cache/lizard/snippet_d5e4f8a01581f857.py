def make_statement(self, action, mention):
    statement_generator, is_direct = geneways_action_to_indra_statement_type(
        mention.actiontype, action.plo)
    if statement_generator is None:
        return None
    text = None
    if self.get_ft_mention:
        try:
            content, content_type = get_full_text(mention.pmid, 'pmid')
            if content is not None:
                ftm = FullTextMention(mention, content)
                sentences = ftm.find_matching_sentences()
                if len(sentences) == 1:
                    text = sentences[0]
        except Exception:
            logger.warning('Could not fetch full text for PMID ' + mention.pmid
                )
    epistemics = dict()
    epistemics['direct'] = is_direct
    annotations = mention.make_annotation()
    annotations['plo'] = action.plo
    evidence = Evidence(source_api='geneways', source_id=mention.
        actionmentionid, pmid=mention.pmid, text=text, epistemics=
        epistemics, annotations=annotations)
    upstream_agent = get_agent(mention.upstream, action.up)
    downstream_agent = get_agent(mention.downstream, action.dn)
    return statement_generator(upstream_agent, downstream_agent, evidence)