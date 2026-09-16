def ProcessLine(filename, file_extension, clean_lines, line, include_state,
    function_state, nesting_state, error, extra_check_functions=[]):
    raw_lines = clean_lines.raw_lines
    ParseNolintSuppressions(filename, raw_lines[line], line, error)
    nesting_state.Update(filename, clean_lines, line, error)
    CheckForNamespaceIndentation(filename, nesting_state, clean_lines, line,
        error)
    if nesting_state.InAsmBlock():
        return
    CheckForFunctionLengths(filename, clean_lines, line, function_state, error)
    CheckForMultilineCommentsAndStrings(filename, clean_lines, line, error)
    CheckStyle(filename, clean_lines, line, file_extension, nesting_state,
        error)
    CheckLanguage(filename, clean_lines, line, file_extension,
        include_state, nesting_state, error)
    CheckForNonConstReference(filename, clean_lines, line, nesting_state, error
        )
    CheckForNonStandardConstructs(filename, clean_lines, line,
        nesting_state, error)
    CheckVlogArguments(filename, clean_lines, line, error)
    CheckPosixThreading(filename, clean_lines, line, error)
    CheckInvalidIncrement(filename, clean_lines, line, error)
    CheckMakePairUsesDeduction(filename, clean_lines, line, error)
    CheckDefaultLambdaCaptures(filename, clean_lines, line, error)
    CheckRedundantVirtual(filename, clean_lines, line, error)
    CheckRedundantOverrideOrFinal(filename, clean_lines, line, error)
    for check_fn in extra_check_functions:
        check_fn(filename, clean_lines, line, error)