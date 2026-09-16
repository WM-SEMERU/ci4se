def print_page(text):
    color_re = re.compile('\\[(?P<color>[FB]G_[A-Z_]+|NORMAL)\\]')
    width = max([len(strip_colors(x)) for x in text.splitlines()])
    print('\n' + hbar(width))
    for line in text.splitlines():
        if line == '[HBAR]':
            print(hbar(width))
            continue
        tail = width - len(strip_colors(line))
        sys.stdout.write('| ')
        previous = 0
        end = len(line)
        for match in color_re.finditer(line):
            sys.stdout.write(line[previous:match.start()])
            set_color(match.groupdict()['color'])
            previous = match.end()
        sys.stdout.write(line[previous:end])
        sys.stdout.write(' ' * tail + ' |\n')
    print(hbar(width))