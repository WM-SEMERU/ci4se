def compound_statements(logical_line):
    line = logical_line
    found = line.find(':')
    if -1 < found < len(line) - 1:
        before = line[:found]
        if before.count('{') <= before.count('}') and before.count('['
            ) <= before.count(']') and not re.search('\\blambda\\b', before):
            return found, 'E701 multiple statements on one line (colon)'
    found = line.find(';')
    if -1 < found:
        return found, 'E702 multiple statements on one line (semicolon)'