def get_version_relationship(ver_str1, ver_str2):
    v1_type = TokenType.DIGIT
    v2_type = TokenType.DIGIT
    v1_tok = 0
    v2_tok = 0
    if ver_str1 is None and ver_str2 is None:
        return ComparisonResult.equal_to
    if ver_str1 is None and ver_str2 is not None:
        return ComparisonResult.less_than
    if ver_str1 is not None and ver_str2 is None:
        return ComparisonResult.greater_than
    while (v1_type == v2_type and v1_type != TokenType.END and v1_type !=
        TokenType.INVALID and v1_tok == v2_tok):
        v1_tok, v1_type, ver_str1 = get_token(v1_type, ver_str1)
        v2_tok, v2_type, ver_str2 = get_token(v2_type, ver_str2)
    if v1_tok < v2_tok:
        return ComparisonResult.less_than
    if v1_tok > v2_tok:
        return ComparisonResult.greater_than
    if v1_type == v2_type:
        return ComparisonResult.equal_to
    if v1_type == TokenType.SUFFIX and get_token(v1_type, ver_str1)[0] < 0:
        return ComparisonResult.less_than
    if v2_type == TokenType.SUFFIX and get_token(v2_type, ver_str2)[0] < 0:
        return ComparisonResult.greater_than
    if v1_type > v2_type:
        return ComparisonResult.less_than
    if v2_type > v1_type:
        return ComparisonResult.greater_than
    return ComparisonResult.equal_to