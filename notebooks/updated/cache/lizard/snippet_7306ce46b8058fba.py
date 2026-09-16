def _check_conditional_statement(statement, num_collections):
    correct_var = list(ascii_lowercase)[:num_collections]
    st_statement = BaseCollection._remove_operators(statement)
    parsed_st = [s for s in st_statement if s.isalpha()]
    for var in parsed_st:
        if var not in correct_var:
            raise ValueError(
                """Invalid conditional statement: {}
 Statement should be a valid Python statement and the variables should be named as follows: {}"""
                .format(statement, ', '.join(correct_var)))
    return correct_var