def length_longest_path(input):
    curr_len, max_len = 0, 0
    stack = []
    for s in input.split('\n'):
        print('---------')
        print('<path>:', s)
        depth = s.count('\t')
        print('depth: ', depth)
        print('stack: ', stack)
        print('curlen: ', curr_len)
        while len(stack) > depth:
            curr_len -= stack.pop()
        stack.append(len(s.strip('\t')) + 1)
        curr_len += stack[-1]
        print('stack: ', stack)
        print('curlen: ', curr_len)
        if '.' in s:
            max_len = max(max_len, curr_len - 1)
    return max_len