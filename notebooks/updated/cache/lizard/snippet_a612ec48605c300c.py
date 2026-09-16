def splitCallsOntoSeparateLines(icNames, icMethod, source):
    callIndices = [(node.func.col_offset if hasattr(node, 'func') else node
        .col_offset) for node in ast.walk(ast.parse(source)) if
        isAstNodeIceCreamCall(node, icNames, icMethod)]
    lines = splitStringAtIndices(source, callIndices)
    sourceWithNewlinesBeforeInvocations = joinContinuedLines(lines)
    return sourceWithNewlinesBeforeInvocations