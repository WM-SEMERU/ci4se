def tupleize(self, contents):
    global CPP_Expression, Table
    contents = line_continuations.sub('', contents)
    cpp_tuples = CPP_Expression.findall(contents)
    return [((m[0],) + Table[m[0]].match(m[1]).groups()) for m in cpp_tuples]