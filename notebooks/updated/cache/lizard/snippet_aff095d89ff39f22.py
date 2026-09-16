def is_background_knowledge(stmt):
    any_background = False
    for ev in stmt.evidence:
        epi = ev.epistemics
        if epi is not None:
            sec = epi.get('section_type')
            if sec is not None and sec not in background_secs:
                return False
            elif sec in background_secs:
                any_background = True
    return any_background