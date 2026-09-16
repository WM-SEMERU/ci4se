def converse(self):
    parser = argparse.ArgumentParser(description=
        'Initiate a conversation with a trained dialogue model')
    self.init_converse_args(parser)
    args = parser.parse_args(sys.argv[2:])
    args.config = ConfigurationLoader(args.config).load().conversation_config
    print(CLI_DIVIDER + '\n')
    Conversant(**vars(args)).run()