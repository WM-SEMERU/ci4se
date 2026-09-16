def pprint_int_dict(int_dict, indent=4, descending=False):
    sorted_tup = sorted(int_dict.items(), key=lambda x: x[1])
    if descending:
        sorted_tup.reverse()
    print('{')
    for tup in sorted_tup:
        print('{}{}: {}'.format(' ' * indent, tup[0], tup[1]))
    print('}')