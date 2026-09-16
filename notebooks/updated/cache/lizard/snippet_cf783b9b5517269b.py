def main():
    arguments = docopt(main.__doc__)
    if arguments.get('--version'):
        print('with {}'.format(withtool.__version__))
        sys.exit()
    while True:
        sub = yield from get_prompt(arguments['<command>'])
        call = '{cmd} {sub}'.format(cmd=arguments['<command>'], sub=sub)
        run(call)