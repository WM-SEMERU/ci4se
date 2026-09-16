def title_line(text):
    columns = shutil.get_terminal_size()[0]
    start = columns // 2 - len(text) // 2
    output = '=' * columns + '\n\n' + ' ' * start + str(text
        ) + '\n\n' + '=' * columns + '\n'
    return output