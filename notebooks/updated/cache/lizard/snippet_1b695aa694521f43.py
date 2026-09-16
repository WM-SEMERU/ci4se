def get_active_forms_state(self):
    for term in self._isolated_terms:
        act = term.find('features/active')
        if act is None:
            continue
        if act.text == 'TRUE':
            is_active = True
        elif act.text == 'FALSE':
            is_active = False
        else:
            logger.warning('Unhandled term activity feature %s' % act.text)
        agent = self._get_agent_by_id(term.attrib['id'], None)
        if not isinstance(agent, Agent):
            continue
        if _is_base_agent_state(agent):
            continue
        agent.activity = None
        text_term = term.find('text')
        if text_term is not None:
            ev_text = text_term.text
        else:
            ev_text = None
        ev = Evidence(source_api='trips', text=ev_text, pmid=self.doc_id)
        st = ActiveForm(agent, 'activity', is_active, evidence=[ev])
        self.statements.append(st)