def isLevel2(edtf_candidate):
    if '[' in edtf_candidate or '{' in edtf_candidate:
        result = edtf_candidate == level2Expression
    elif ' ' in edtf_candidate:
        result = False
    else:
        result = edtf_candidate == level2Expression
    return result