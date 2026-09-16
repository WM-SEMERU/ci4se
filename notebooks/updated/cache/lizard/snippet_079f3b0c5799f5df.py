def _svcomp_score(category, result):
    assert result is not None
    result_class = get_result_classification(result)
    if category == CATEGORY_CORRECT_UNCONFIRMED:
        if result_class == RESULT_CLASS_TRUE:
            return _SCORE_CORRECT_UNCONFIRMED_TRUE
        elif result_class == RESULT_CLASS_FALSE:
            return _SCORE_CORRECT_UNCONFIRMED_FALSE
        else:
            assert False
    elif category == CATEGORY_CORRECT:
        if result_class == RESULT_CLASS_TRUE:
            return _SCORE_CORRECT_TRUE
        elif result_class == RESULT_CLASS_FALSE:
            return _SCORE_CORRECT_FALSE
        else:
            assert False, result
    elif category == CATEGORY_WRONG:
        if result_class == RESULT_CLASS_TRUE:
            return _SCORE_WRONG_TRUE
        elif result_class == RESULT_CLASS_FALSE:
            return _SCORE_WRONG_FALSE
        else:
            assert False
    else:
        return _SCORE_UNKNOWN