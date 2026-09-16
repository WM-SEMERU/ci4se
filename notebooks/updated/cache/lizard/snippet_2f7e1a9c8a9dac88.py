def get_sql_state(self, state):
    if not hasattr(state, 'sql_state'):
        setattr(state, 'sql_state', SQLStateGraph())
    return state.sql_state