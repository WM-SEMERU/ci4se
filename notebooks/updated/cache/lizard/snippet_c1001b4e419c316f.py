def CheckHeader(context, header, include_quotes='<>', language=None):
    prog_prefix, hdr_to_check = createIncludesFromHeaders(header, 1,
        include_quotes)
    res = SCons.Conftest.CheckHeader(context, hdr_to_check, prog_prefix,
        language=language, include_quotes=include_quotes)
    context.did_show_result = 1
    return not res