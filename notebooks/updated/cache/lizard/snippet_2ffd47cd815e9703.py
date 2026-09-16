def replace(code, pattern, goal):
    finder = similarfinder.RawSimilarFinder(code)
    matches = list(finder.get_matches(pattern))
    ast = patchedast.get_patched_ast(code)
    lines = codeanalyze.SourceLinesAdapter(code)
    template = similarfinder.CodeTemplate(goal)
    computer = _ChangeComputer(code, ast, lines, template, matches)
    result = computer.get_changed()
    if result is None:
        return code
    return result