def main():
    parser = ArgumentParser()
    parser.add_argument('direction', choices=('up', 'down', 'left', 'right',
        'next', 'prev'), help='Direction to put the focus on')
    args = parser.parse_args()
    tree = i3Tree()
    con = None
    if args.direction in ('next', 'prev'):
        con = cycle_outputs(tree, args.direction)
    else:
        con = cycle_windows(tree, args.direction)
    if con:
        i3.focus(con_id=con.id)