def _is_statement_in_list(new_stmt, old_stmt_list):
    for old_stmt in old_stmt_list:
        if old_stmt.equals(new_stmt):
            return True
        elif old_stmt.evidence_equals(new_stmt) and old_stmt.matches(new_stmt):
            if isinstance(new_stmt, Complex):
                agent_pairs = zip(old_stmt.sorted_members(), new_stmt.
                    sorted_members())
            else:
                agent_pairs = zip(old_stmt.agent_list(), new_stmt.agent_list())
            for ag_old, ag_new in agent_pairs:
                s_old = set(ag_old.db_refs.items())
                s_new = set(ag_new.db_refs.items())
                if s_old == s_new:
                    continue
                if s_old > s_new:
                    return True
                if s_new > s_old:
                    ag_old.db_refs.update(ag_new.db_refs)
                    return True
                if _fix_different_refs(ag_old, ag_new, 'CHEBI'):
                    return _is_statement_in_list(new_stmt, old_stmt_list)
                if _fix_different_refs(ag_old, ag_new, 'UMLS'):
                    return _is_statement_in_list(new_stmt, old_stmt_list)
                logger.warning(
                    'Found an unexpected kind of duplicate. Ignoring it.')
                return True
            return True
        elif old_stmt.get_hash(True, True) == new_stmt.get_hash(True, True):
            e_old = old_stmt.evidence[0]
            e_new = new_stmt.evidence[0]
            if e_old.annotations['last_verb'] is None:
                e_old.annotations['last_verb'] = e_new.annotations['last_verb']
            if e_old.get_source_hash(True) == e_new.get_source_hash(True):
                return True
    return False