def pretty(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent + 1)
        else:
            sys.stderr.write('  ' * (indent + 1) + str(value) + '\n')