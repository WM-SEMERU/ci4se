def symbol_list(what_list):
    if what_list is 'list1':
        symbol = ['ro', 'bo', 'ko', 'go', 'mo', 'r-', 'b-', 'k-', 'g-',
            'm-', 'r--', 'b--', 'k--', 'g--', 'r1']
    elif what_list is 'list2':
        symbol = ['r-', 'b--', 'g-.', 'k:', 'md', '.', 'o', 'v', '^', '<',
            '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+']
    elif what_list is 'lines1':
        symbol = ['b--', 'k--', 'r--', 'c--', 'm--', 'g--', 'b-', 'k-',
            'r-', 'c-', 'm-', 'g-', 'b.', 'b-.', 'k-.', 'r-.', 'c-.', 'm-.',
            'g-.', 'b:', 'k:', 'r:', 'c:', 'm:', 'g:']
    elif what_list is 'lines2':
        symbol = ['g:', 'r-.', 'k-', 'b--', 'k-.', 'b+', 'r:', 'b-', 'c--',
            'm--', 'g--', 'r-', 'c-', 'm-', 'g-', 'k-.', 'c-.', 'm-.',
            'g-.', 'k:', 'r:', 'c:', 'm:', 'b-.', 'b:']
    return symbol